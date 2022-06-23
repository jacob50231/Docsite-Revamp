import os
from yaml import safe_load
from markdown import markdown
from bs4 import BeautifulSoup
from jinja2 import Template
import sys

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
        self.read_yaml()
    
    def read_yaml(self):
        with open(self.config_file) as f:
            yml = safe_load(f)

        # Get Home Directory
        self.home_directory = yml['site_loc']

        # Get Location of HTML Template
        self.template_path = self.home_directory + '/' + yml['template_path']

        # Get Pages
        for d in yml['pages']:
            for k,v in d.items():
                source_list = []
                print(k)
                for d2 in v:
                    source_list.append(list(d2.values())[0])
                self.pages[k] = source_list
    
        # Get CSS file locations
        for f in yml['css_files']:
            self.css_files.append(self.home_directory + "/" + f)

        return
    
    
    def write_pages(self):

        # Clear output directory if it exists
        try:
            rmdir("output")
        except Exception:
            pass
        os.mkdir("output")
        
        # Iterate through self.pages dictionary and write each to file.
        for k,v in self.pages.items():
            os.mkdir("output/" + k)
            for loc in v:
                print(k.replace(" ","_") + "/" + loc.split("/")[-1])
                self.write_to_template("docs/" + loc, "output/" + k + "/" + loc.split("/")[-1].replace("md","html"))

        return


    
            
    def write_to_template(self,markdown_path,output_path):

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


        # Get Sidebar data (Needs fixing)
        soup = BeautifulSoup(content,'html.parser')

        sidebar = ""
        for h2 in soup.find_all("h2"):
            val = str(h2.string)
            h2['id'] = val
            sidebar += f"<li><a href='#{val}'>{val}</a></li>"


        # Render output and write to file
        output = template.render(content = content, sidebar = sidebar, css = self.css_files)

        with open(output_path, 'w') as f:
            f.write(output)

        return


if __name__ == "__main__":
    pages = Pages('docs.yml')
    pages.write_pages()
