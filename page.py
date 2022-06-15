import os
from genericpath import exists
from turtle import title
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader,PackageLoader
import os
from datetime import datetime
import logging
import http
import jinja2
from ruamel.yaml import YAML
from slugify import slugify


"""This class builds the page object from the mkdocs.yml file."""

class Pages:
    def __init__(self,file):
        #self.directory = directory
        self.pages = []
        self.mkdocs_config = file
        self.get_pages()



    def get_pages(self):
        assert exists(self.mkdocs_config), "mkdocs.yml file does not exist"
        with open(self.mkdocs_config,'r') as yaml_file:
            yaml = YAML(typ='safe')
            mkdocs_config = yaml.load(yaml_file)
            for page in mkdocs_config['pages']:
                self.pages.append(page)
            return self.pages


        

    def build_dir(self,app_name):
        for page in self.pages:
            #Get pages from the pages key in the mkdocs file which returns list of dictionaries
            for k,v in page.items():
                if isinstance(v,list):
                    for item in v:
                        if isinstance(item,dict):
                            for k,v in item.items():
                                file = v.split('/')[-1].split('.')[0]
                                filename = v.split('/')[-1]
                                if filename.endswith('.md'):
                                    v = v.split('/')[:-1]
                                    print(filename)     
                                    #merge list elements into paths
                                    v = '/'.join(v)
                                    os.makedirs(os.path.join('dist',v),exist_ok=True)
                                    filename = open(os.path.join('docs',v,filename),'r')
                                    html = markdown(filename.read(),extras=['fenced-code-blocks','tables','metadata'])
                                    print(html)
                                    env = Environment(loader=PackageLoader(app_name, 'templates'))
                                    base_template = env.get_template('template.html')
                                    base_metadata = html.metadata
                                    with open(self.mkdocs_config) as f:
                                       yaml = YAML(typ='safe')
                                       mkdocs_config = yaml.load(f)
                                    base_html = base_template.render(page = base_metadata,
                                                                    #page_title = html.metadata['page_title'],
                                                                    config = mkdocs_config,
                                                                    nav = mkdocs_config['pages'],
                                                                    content = html
                                                                 )
                                    parsed_file = open(os.path.join('dist',v,self.make_html(file)), 'w')
                                    parsed_file.write(base_html)
                file = v.split('/')[-1].split('.')[0]
                print(file)
                filename = v
                v = v.split('/')[:-1]
                os.makedirs(os.path.join('dist',k),exist_ok=True)
                filename = open(os.path.join('docs',k,filename),'r')
                html = markdown(filename.read(),extras=['fenced-code-blocks','tables','metadata'])
                print(html)
                env = Environment(loader=PackageLoader(app_name, 'templates'))
                base_template = env.get_template('template.html')
                base_metadata = html.metadata
                with open(self.mkdocs_config) as f:
                    yaml = YAML(typ='safe')
                    mkdocs_config = yaml.load(f)
                base_html = base_template.render(page = base_metadata,
                                                #page_title = html.metadata['page_title'],
                                                config = mkdocs_config,
                                                nav = mkdocs_config['pages'],
                                                content = html
                                                )
                parsed_file =  open(os.path.join('dist',k,self.make_html(file)), 'w')
                parsed_file.write(base_html)

    @staticmethod
    def make_html(file):
        return slugify(file)+'.html'




    def build_mkdocs(self):
        self.get_pages()
        self.build_dir('page')
        




class Page:
    def __init__(self,pages,html_name):
        self.pages = pages
        self.html_name = html_name
        self.page_name = ''


if __name__=='__main__':
    pages = Pages('mkdocs.yml')
    pages.build_mkdocs()