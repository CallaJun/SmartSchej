#!/usr/bin/env python
import jinja2
import logging
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        template = jinja_environment.get_template('views/home.html')
        self.response.out.write(template.render(template_values))

class NextHandler(webapp2.RequestHandler):
    def get(self):  
        template_values = {
        }
        eventname = self.request.get('input')

        template_values['eventname'] = eventname

        template = jinja_environment.get_template('views/next.html')
        self.response.out.write(template.render(template_values))

routes = [('/', HomeHandler),('/next', NextHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 