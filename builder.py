import glob
import os
from jinja2 import Environment, FileSystemLoader

colors = { 
           'black' : '#1d1d1d',
           'blue' : '#4465e9',
           'green' : '#099268',
           'grey' : '#9fa8b2',
           'light-blue': '#4ba1f1',
           'light-green': '#4cb05e',
           'light-red': '#f87777',
           'light-violet': '#e085f4',
           'orange': '#e16919',
           'red': '#e03131',
           'violet': '#ae3ec9',
           'yellow': '#f1ac4b',
           'white': '#FFFFFF'
         }
for elt in os.environ.get('colorsicons', "").split(";"):
    if ':' in elt:
        colors[elt.split(":")[0]] = elt.split(":")[1]


env = Environment(loader=FileSystemLoader("."))
templs = ['App.tsx', 'icons-tool-util.tsx']
icons=[icon.split('/')[-1] for icon in glob.glob("./icons/*.svg")]

for templ in templs:
    with open(templ, 'w') as file:
        template = env.get_template("%s.tmp" % templ)
        file.write(template.render(icons=icons))

for icon in icons:
    with open("./icons/%s" % icon, 'r') as fileicon:
        data = fileicon.read()
        for color in colors:
            with open("./icons/%s-%s.svg" % (icon.split('.')[0], color), 'w') as filecolor:
                filecolor.write(data.replace('currentColor', colors[color]))
        