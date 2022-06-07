from markdown import markdown
from bs4 import BeautifulSoup
import sys

def write_to_template(template_path,markdown_path,output_path):

    with open(template_path,'r') as f:
        template = f.read()

    with open(markdown_path,'r') as f:
        content = f.read()
    content = markdown(content, extensions=['markdown.extensions.tables',"markdown.extensions.fenced_code"])
    content = content.replace("</h1>","</h1><hr>")
    content = content.replace("<h1>",'<h1><i class="fas fa-book"></i>   ')
    content = content.replace("<table>","<table class='table'>")

    soup = BeautifulSoup(content,'html.parser')

    sidebar = ""
    for h2 in soup.find_all("h2"):
        val = str(h2.string)
        h2['id'] = val
        sidebar += f"<li><a href='#{val}'>{val}</a></li>"


    content = str(soup)
    output = template.replace("{{{",content).replace("}}}","")
    output = output.replace("{{",sidebar).replace("}}","")

    with open(output_path, 'w') as f:
        f.write(output)


if __name__ == "__main__":

    template_path = sys.argv[1]
    markdown_path = sys.argv[2]
    output_path = sys.argv[3]

    write_to_template(template_path,markdown_path,output_path)
