from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re

SCOPES = ['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive']

class Slides:
    def __init__(self):
        creds = None
        
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=19999)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('slides', 'v1', credentials=creds)
        self.drive_service = build('drive', 'v3', credentials=creds)

    def create(self, title):
        body = {
            'title': '%s (made with QuikSlide)' % title
        }
        make = self.service.presentations().create(body=body).execute()
        self.presentation = make
        self.id = make.get('presentationId')

    def share(self, email):
        def callback(request_id, response, exception):
            if exception:
                # Handle error
                print(exception)
            else:
                print(f"Slideshow Successfully Shared With Id {response.get('id')}")

        batch = self.drive_service.new_batch_http_request(callback=callback)
        user_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': email
        }
        batch.add(self.drive_service.permissions().create(fileId=self.id, body=user_permission, fields='id', sendNotificationEmail=False,))
        batch.execute()

    def update(self, objects):
        body = { "requests": objects }
        response = self.service.presentations() \
                       .batchUpdate(presentationId=self.id, body=body) \
                       .execute()
        return response
    