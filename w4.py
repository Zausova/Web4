from jinja2 import Environment, FileSystemLoader
from webob import Request
import os

mass = [
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js',
    'main.css',
    'bootstrap.css',
    'normalize.css',
    ]
js = []
css = []


def app(environ, start_response):
    response_code = '200 OK'
    response_type = ('Content-Type', 'text/HTML')
    start_response(response_code, [response_type])

    for elem in mass:
        elemspl = elem.split('.')
        if len(elemspl[1]) == 2:
            js.append(elem)
        elif len(elemspl[1]) == 3:
            css.append(elem)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')
    print(template.render(css0=css, js0=js))

reqTwo = Request.blank('index.html')
print(reqTwo.get_response(app))
