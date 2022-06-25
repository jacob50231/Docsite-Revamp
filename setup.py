import sys
from page import Pages
#setup the page module for use in the CLI

if __name__ == '__main__':
    import argparse

    my_parser = argparse.ArgumentParser(allow_abbrev=False)
    my_parser.add_argument('--project_home', action='store', type=str, required=True)
    my_parser.add_argument('--docs_file', action='store', type=str, required=True)
    args = my_parser.parse_args()

    #create a new Pages object
    pages = Pages(project_home_title=args.project_home,config_file= args.docs_file)
    #Write the pages
    pages.write_pages()


