import os
from yaml import safe_load
from markdown import markdown
from bs4 import BeautifulSoup
from jinja2 import Template
import sys
from pathlib import Path
import yaml
from slugify import slugify


def rmdir(dir):
    path = os.path.normpath(dir)
    for root, dirs, files in os.walk(path,topdown=False):
        for f in files:
            os.remove(os.path.join(root,f))
        for d in dirs:
            os.rmdir(os.path.join(root,d))

    os.rmdir(dir)
    return



class Pages:
        
    def __init__(self,config_file):
        self.config_file = config_file
        self.pages = {}
        self.css_files = []
        self.js_files = []
        self.links = []
        self.siblings = {}
        self.link_data = {}
        self.search_obj = []
        self.pedia_obj = {}
        self.read_yaml()
        self.nav_pages = self.get_nav_pages()
    
    def read_yaml(self):
        with open(self.config_file) as f:
            yml = safe_load(f)

        # Get Home Directory
        self.home_directory = yml['site_loc']
        
        # Get Site URL (Should be same as home directory for development)
        self.site_url = yml['site_url']

        # Get Location of HTML Template
        self.template_path = os.path.join(self.home_directory,yml['template_path'])
        self.encyclopedia_path = os.path.join(self.home_directory,yml['encyclopedia_path'])
        self.index_template = os.path.join(self.home_directory,yml['index_template'])
        
        # Get GDC Logo location
        self.logo = os.path.join(self.home_directory,yml['logo'])

        # Get Pages
        for d in yml['pages']:
            group = list(d.keys())[0]
            self.pages[group] = d[group]
    
        # Get CSS file locations
        for f in yml['css_files']:
            self.css_files.append(os.path.join(self.site_url, f))

        # Get Js Files
        for f in yml['js_files']:
            self.js_files.append(os.path.join(self.site_url, f))
            
        self.link_data = self.pages

        return

    def get_nav_pages(self):
        nav_pages = {}
        for group in self.pages.keys():
            for page in self.pages[group]:

                # Get Page Name
                pname = list(page.keys())[0]

                # Get Page Location
                ploc = page[pname].replace('md','html')

                # Append to navigation pages object for use in top bar
                if group in list(nav_pages.keys()):
                    nav_pages[group].append({pname:f"{self.site_url}/output/{ploc}"})               
                else:
                    nav_pages[group] =[{pname:f"{self.site_url}/output/{ploc}"}]
        return nav_pages
    
    
    def write_encyclopedia(self,css,logo,pagename,encyclopedia_path,pedia_object,js,nav_pages):
        with open(encyclopedia_path,'r') as f:
            template = f.read()
            template = Template(template)
        output = template.render(css=css,logo=logo,pagename=pagename,encyclopedia_pages=pedia_object,js=js,nav_pages=nav_pages)
        with open(os.path.join(self.home_directory,'output','Encyclopedia' , "index.html"), 'w') as f:
            f.write(output)
    
    def write_homepage(self):
        with open(self.index_template,'r') as f:
            template = f.read()
            template = Template(template)
        output = template.render(nav_pages = self.nav_pages, js = self.js_files)
        with open(os.path.join(self.home_directory,'output', "index.html"), 'w') as f:
            f.write(output)
        os.remove(os.path.join(self.home_directory,'output',"index.md"))

    
    def write_pages(self):

        # Clear output directory if it exists
        try:
            rmdir("output")
        except Exception:
            pass

        
        # Copy markdown folder
        os.system("cp -R docs output")
        
        # Iterate through self.pages dictionary and write each markdown file to template
        for group in self.pages.keys():
            print(group)

            if group == "Home":
                self.write_homepage()

            else:
            
                for page in self.pages[group]:

                    # Get name of current page, and it's location
                    pagename = list(page.keys())[0]
                    pageloc = page[pagename]

                    # Print page name, and location of markdown file 
                    print(f"Writing Markdown🔄: {pagename} to {self.home_directory + pageloc}")

                    # Write to template and remove markdown file
                    self.write_to_template("output/" + pageloc, "output/" + pageloc.replace("md","html"), group, pagename, )
                    os.remove("output/" + pageloc)
                
                if group == "EncyclopediaEntries":
                    for page in self.pages["EncyclopediaEntries"]:
                        # Get name of current page, and it's location
                        pagename = list(page.keys())[0]
                        pageloc = page[pagename]
                        
                        #slugify the url
                        slug = slugify(pageloc.split('/')[0] +'/' + pageloc.split('/')[-1]).replace("-md","")
                        self.pedia_obj[pagename] = self.site_url + '/' + slug
                    self.write_encyclopedia(css = self.css_files, logo = self.logo, pagename = pagename,encyclopedia_path = self.encyclopedia_path,pedia_object = self.pedia_obj,js=self.js_files,nav_pages = self.nav_pages)

        return

            
    def write_to_template(self,markdown_path,output_path,group,pagename):

        # Get Jinja HTML Template
        with open(self.template_path,'r') as f:
            template = f.read()
            template = Template(template)

        # Read markdown to string
        with open(markdown_path,'r') as f:
            content = f.read()

        # Convert markdown to html and add extras
        content = markdown(content, extensions=['markdown.extensions.tables',"markdown.extensions.fenced_code"])
        content = content.replace("</h1>","</h1><hr>")
        content = content.replace("<h1>",'<h1><i class="fas fa-book"></i>   ')
        content = content.replace("<table>","<table class='table'>")



        # Get Current page information for scroll-to section of sidebar
        soup = BeautifulSoup(content,'html.parser')

        # Update Search Object
        headers = soup.find_all(['h1','h2'])
        for header in headers:
            self.search_obj.append({'name':header.text, 'location':output_path})

        # Create Sidebar
        sidebar_inner = ""
        for h2 in soup.find_all("h2"):
            val = str(h2.string)
            h2['id'] = val # add id for sidebar to scroll to
            sidebar_inner += f"<li><a href='#{val}'>{val}</a></li>"
        
        # Iterate through current group and place every page into sidebar
        sidebar = ""
        for page in self.pages[group]:
            pname = list(page.keys())[0]
            ploc = page[pname].replace('md','html')
            if pname == pagename:
                sidebar += f'<li class="main"><a href="{self.site_url}/output/{ploc}">{pname}</a></li>'
                sidebar += "<ul>"
                sidebar += sidebar_inner
                sidebar += "</ul>"
            else:
                sidebar += f'<li class="inactive"><a href="{self.site_url}/output/{ploc}">{pname}</a></li>'

        # Render output and write to file
        content = str(soup)
        output = template.render(content = content, sidebar = sidebar, css = self.css_files, logo = self.logo, pagename = pagename, site_url = self.site_url, nav_pages = self.nav_pages)

        with open(output_path, 'w') as f:
            f.write(output)

        return

if __name__ == "__main__":
    pages = Pages('docs.yml')
    pages.write_pages()
    with open("tmp.js",'w') as f:
        f.write("const searchData = " + str(pages.search_obj))
    print(pages.pages)
