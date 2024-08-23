import glob
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
templs = ['App.tsx', 'icons-tool-util.tsx']
icons=[icon.split('/')[-1] for icon in glob.glob("./icons/*.svg")]

for templ in templs:
    with open(templ, 'w') as file:
        template = env.get_template("%s.tmp" % templ)
        file.write(template.render(icons=icons))