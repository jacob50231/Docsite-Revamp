# GDC Documentation Site Rebuild Project (GSoC)
The purpose of this project is to rebuild the documentation of the GDC website to be more responsive, and more manageable for future developers to maintain. This will be done by replacing the current mkdocs framework with a barebones python script used to build the static site. Due to the complexity of the current site, very little of the code is salvageable, and we will need to reverse engineer a lot of the css styling (much of this is already done). The remainder of this project is largely split up into three parts.

1. Markdown Section: Here we need to update the python file in this directory to follow the directory structure laid out in the `pages:` section. 

2. Rebuild the data dictionary: This will be extremely intensive in javascript programming and I expect it to take up the majority of time on this project.

3. Rebuild the encyclopedia. This is more front-end and css heavy with some javascript being required for functionality. This shouldn't be too bad.

Beyond this, we just need to make some basic front end changes to the code.

# Getting Started
Start by navigating to this directory in your command line, and create a new virtual python environment to work in by typing:
`python3 -m venv gdc-docs-env` (Note: Depending on your system you may need to replace "python3" with "python")

And activate it with:
`source gdc-docs-env/bin/activate` (Note: This can be deactivated at any time by typing deactivate into the command line)

From here install required dependencies:
`pip install -r requirements.txt`

And you are ready to run the python file. Currently it is just a proof of concept only working on one file, it takes as inputs, in order, the path of the template, the path of the markdown file, and the path of the output file. An example of running this looks as follows:
`python3 markdownhtml.py templates/template.html markdown/Getting_Started.md output.html`



