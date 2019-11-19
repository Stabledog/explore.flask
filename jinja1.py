#!/opt/bb/bin/python3.7

from jinja2 import Template

t = Template("Hello {{something}}")

print(t.render(something="World"))

t = Template("Favorite numbers: {% for n in [1,2,3]%}{{n}} " " {% endfor %}")

print(t.render()

