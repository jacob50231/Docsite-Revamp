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
    def __init__(self,config_file,project_home_title):
        self.config_file = config_file
        self.pages = {}
        self.css_files = []
        self.links = []
        self.link_data = {}
        self.base_dir = os.path.join(Path(__file__).resolve().parent.parent,project_home_title)
        self.read_yaml()
    
    def read_yaml(self):
        with open(self.config_file) as f:
            yml = safe_load(f)

        # Get Home Directory
        yml['site_loc'] = self.base_dir
        self.home_directory = yml['site_loc']
        # Get Site URL (Should be same as home directory for development)
        self.site_url = self.base_dir

        # Get Location of HTML Template
        self.template_path = os.path.join(self.home_directory,yml['template_path'])
        
        # Get GDC Logo location
        self.logo = os.path.join(self.home_directory,yml['logo'])

        # Get Pages
        for d in yml['pages']:
            group = list(d.keys())[0]
            self.pages[group] = d[group]
    
        # Get CSS file locations
        for f in yml['css_files']:
            self.css_files.append(os.path.join(self.home_directory, f))

        # Get Links
        try:
            with open('links.yml') as link:
                link_yml = safe_load(link)
            self.link_data = link_yml

        except FileNotFoundError:
            print("No links.yml file found. Links will  be generated now.")
            self.write_links_to_yaml()
        finally:
            with open('links.yml') as link:
                link_yml = safe_load(link)
            self.link_data = link_yml
            

        return
    # Write links to links.yml
    def write_links_to_yaml(self):
        for group,page_data in self.pages.items():
            for i in page_data:
                for _,page_loc in i.items():
                    self.links.append({'_'.join(page_loc.split('/')).replace('.md',''):'dist/' +slugify(''.join(page_loc.split('/')[-1])).replace('-md','.html')})
        with open('links.yml','w+') as f:
            yml = safe_load(f)
            for link in self.links:
                yaml.dump(link,f)

        return
    
    
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
            
            for page in self.pages[group]:

                # Get name of current page, and it's location
                pagename = list(page.keys())[0]
                pageloc = page[pagename]

                # Print page name, and location of markdown file 
                print("\t" + pagename + ": " + pageloc)

                # Write to template and remove markdown file
                os.makedirs("output/dist/",exist_ok=True)
                self.write_to_template("output/" + pageloc, "output/" + 'dist/' + slugify(pageloc.split('/')[0] +'/' + pageloc.split('/')[-1]).replace("-md",".html"), group, pagename )
                print('***',pageloc)
                os.remove(os.path.join("output" , pageloc))

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
        output = template.render(content = content, sidebar = sidebar, css = self.css_files, logo = self.logo, pagename = pagename, site_url = self.site_url,link=self.link_data)

        with open(output_path, 'w') as f:
            f.write(output)

        return

# if __name__ == "__main__":
#     pages = Pages('docs.yml','Docsite-Revamp')
#     pages.write_pages()
