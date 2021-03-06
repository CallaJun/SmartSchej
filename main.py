#!/usr/bin/env python
import jinja2
import logging
import os
import webapp2
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
import httplib2
from gdata.apps import service
import atom

flow = OAuth2WebServerFlow(client_id='195549864721-i2juie0n9vvq5g7itrk49a4452easbse.apps.googleusercontent.com',
                           client_secret='12haQegMUPOGvJIa6RDVfhK8',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://example.com/auth_return')

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
        eventname = self.request.get('eventname')
        eventdescription = self.request.get('eventdescription')


        template_values['eventname'] = eventname
        template_values['eventdescription'] = eventdescription
        '''
        created_event = service.events().quickAdd(
            calendarId='primary',
            text=eventname).execute()

        print created_event['id']
        '''

        template = jinja_environment.get_template('views/next.html')
        self.response.out.write(template.render(template_values))

routes = [('/', HomeHandler),('/next', NextHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 