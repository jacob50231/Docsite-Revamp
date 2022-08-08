import os
from yaml import safe_load
from markdown import markdown
from bs4 import BeautifulSoup
from jinja2 import Template
import sys
from pathlib import Path
import yaml
from slugify import slugify
#from playground import add_playground






ROOT_DIR = 'output/dist/'

def rmdir(dir):
    path = os.path.normpath(dir)
    for root, dirs, files in os.walk(path,topdown=False):
        for f in files:
            os.remove(os.path.join(root,f))
        for d in dirs:
            os.rmdir(os.path.join(root,d))

    os.rmdir(dir)
    return


os.makedirs(os.path.join(ROOT_DIR,'encyclopedia/'), exist_ok=True)

def write_encyclopedia(css,logo,pagename,encyclopedia_path,pedia_object,js,nav_pages):
    os.makedirs(os.path.join(ROOT_DIR,'encyclopedia/'), exist_ok=True)
    with open(encyclopedia_path,'r') as f:
        template = f.read()
        template = Template(template)
    output = template.render(css=css,logo=logo,pagename=pagename,encyclopedia_pages=pedia_object,js=js,nav_pages=nav_pages)
    with open(os.path.join(ROOT_DIR,'encyclopedia' , "index.html"), 'w') as f:
        f.write(output)


class Pages:
    def __init__(self,config_file,project_home_title):
        self.config_file = config_file
        self.pages = {}
        self.css_files = []
        self.js_files = []
        self.links = []
        self.siblings = {}
        self.link_data = {}
        self.search_obj = {}
        self.pedia_obj = {}
        self.base_dir = os.path.join(Path(__file__).resolve().parent.parent,project_home_title)
        self.read_yaml()
        self.nav_pages = self.get_nav_pages()
        #self.build_encyclopedia()
    
    def read_yaml(self):
        with open(self.config_file) as f:
            yml = safe_load(f)

        # Get Home Directory
        yml['site_loc'] = self.base_dir
        self.home_directory = self.base_dir
        # Get Site URL (Should be same as home directory for development)
        self.site_url = self.base_dir

        # Get Location of HTML Template
        self.template_path = os.path.join(self.home_directory,yml['template_path'])
        self.encyclopedia_path = os.path.join(self.home_directory,yml['encyclopedia_path'])
        
        # Get GDC Logo location
        self.logo = os.path.join(self.home_directory,yml['logo'])

        # Get Pages
        for d in yml['pages']:
            group = list(d.keys())[0]
            self.pages[group] = d[group]
    
        # Get CSS file locations
        for f in yml['css_files']:
            self.css_files.append(os.path.join('/', f))

        # Get Js Files
        for f in yml['js_files']:
            self.js_files.append(os.path.join('/', f))

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
            self.write_links_to_yaml()
            

        return
    # Write links to links.yml
    def write_links_to_yaml(self):
        for group,page_data in self.pages.items():
            for i in page_data:
                for _,page_loc in i.items():
                    self.links.append({str(page_loc.split('/')[0]+"_"+page_loc.split('/')[-1].replace('.md','')).lower():'dist/' +slugify(''.join(page_loc.split('/')[-1])).replace('-md','' + '/index.html')})
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
            
            for page in self.pages[group]:

                # Get name of current page, and it's location
                pagename = list(page.keys())[0]
                pageloc = page[pagename]

                # Print page name, and location of markdown file 
                #print("\t" + pagename + ": " + pageloc)

                # Write to template and remove markdown file
                slug = slugify(pageloc.split('/')[0] +'/' + pageloc.split('/')[-1]).replace("-md","")
                os.makedirs(ROOT_DIR + slug,exist_ok=True)
                
                #print(self.pages.keys())
                print(f"Writing Markdown🔄: {pagename} to {ROOT_DIR + slug + '/index.html'}")

                self.write_to_template("output/" + pageloc, ROOT_DIR + slug +'/index.html', group, pagename)
                print(f"Done......\nMarkdown written to template✅")
            if group == "EncyclopediaEntries":
                for page in self.pages["EncyclopediaEntries"]:
                    # Get name of current page, and it's location
                    pagename = list(page.keys())[0]
                    pageloc = page[pagename]
                    
                    #slugify the url
                    slug = slugify(pageloc.split('/')[0] +'/' + pageloc.split('/')[-1]).replace("-md","")
                    self.pedia_obj[pagename] = ROOT_DIR + slug

            write_encyclopedia(css = self.css_files, logo = self.logo, pagename = pagename,encyclopedia_path = self.encyclopedia_path,pedia_object = self.pedia_obj,js=self.js_files,nav_pages = self.nav_pages)

                
        os.remove(os.path.join("output" , pageloc))
        #print(self.nav_pages)
        return

    #Build page Siblings 
    def set_page_siblings(self):
        
        siblings = {}
        for group in self.pages.keys():
            siblings_group = []
            for page in self.pages[group]:
                [siblings_group.append(i) for i in page if i != page]
            siblings[group] = siblings_group
           
        for group in siblings.keys():
            a = {}
            for page in siblings[group]:
                current_page = page
                siblings_group = [i for i in siblings[group] if i != current_page]
                a[current_page] = siblings_group
            self.siblings[group] = a
                        
        return
    #Get siblings for current page: Can be used in the sidebar. ! Still needs fixing.
    def get_page_siblings(self,group,page):
        self.set_page_siblings()
        return self.page_siblings[group][page]

    def get_nav_pages(self):
        nav_pages = {}
        for group in self.pages.keys():
            for page in self.pages[group]:
                pname = list(page.keys())[0]
                ploc = page[pname].replace('md','html')
                pageloc = page[pname]
                slug = slugify(pageloc.split('/')[0] +'/' + pageloc.split('/')[-1]).replace("-md","")
                # ?  This  Sub pages in navbar😎
                if group in list(nav_pages.keys()):
                        nav_pages[group].append({pname:f"{ROOT_DIR}{slug}"})               
                else:
                    nav_pages[group] =[]
        # print(nav_pages)
        return nav_pages
        

    def write_to_template(self,markdown_path,output_path,group,pagename):

        # Get Jinja HTML Template
        with open(self.template_path,'r') as f:
            template = f.read()
            template = Template(template)

        # Read markdown to string
        with open(markdown_path,'r') as f:
            content = f.read()

        # Convert markdown to html and add extras
        content = markdown(content, extensions=['markdown.extensions.tables',"markdown.extensions.fenced_code","markdown.extensions.attr_list"])
        content = content.replace("</h1>","</h1><hr>")
        content = content.replace("<h1>",'<h1><i class="fas fa-book"></i>   ')
        content = content.replace("<table>","<table class='table'>")

        #playground_frame = '<iframe src="https://trinket.io/embed/python/10edf791b0?toggleCode=true&runOption=run" width="50%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>'
        soup = BeautifulSoup(content, 'html.parser')
        
         #print(soup.pre.find_next())
        headers = soup.find_all(['h1','h2','h3'])
        for header in headers:
            self.search_obj.update({header.string: output_path})

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
            pageloc = page[pname]
            slug = slugify(pageloc.split('/')[0] +'/' + pageloc.split('/')[-1]).replace("-md","")
            if pname == pagename:
                sidebar += f'<li class="main"><a href="/output/dist/{slug}">{pname}</a></li>'
                
                sidebar += "<ul>"
                sidebar += sidebar_inner
                sidebar += "</ul>"
            else:
                sidebar += f'<li class="inactive"><a href="/output/dist/{slug}">{pname}</a></li>'
        # for code_tag in soup.find_all('code',attrs={'class':'language-python'}):
        #     new_tag = soup.new_tag('py-repl')
        #     new_tag.string = code_tag.string
        #     code_tag.parent.insert_after(new_tag)

        # Render output and write to file

        content = str(soup)
        output = template.render(content = content, sidebar = sidebar, css = self.css_files, logo = self.logo, pagename = pagename, site_url = self.site_url,link=self.link_data,search_obj = self.search_obj,nav_pages=self.nav_pages)
        #print(output_path)
        with open(output_path, 'w') as f:
            f.write(output)
        
        return
