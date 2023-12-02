import datetime
import pickle
import os.path
from pathlib import Path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# CREDENTIALS_FILE = './creds/service.json'
CREDENTIALS_FILE = Path(os.getenv('GOOGLE_CREDENTIALS_JSON'))
PICKLE_FILE = Path(os.getenv('GOOGLE_CREDENTIALS_PICKLE'))

def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if PICKLE_FILE.exists():
        # load pickle
        creds = pickle.loads(PICKLE_FILE.read_bytes())
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE.read_text(), SCOPES)
            creds = flow.run_local_server(port=0)
            # save new pickle
            pickle.dumps(PICKLE_FILE.read_bytes())

    service = build('calendar', 'v3', credentials=creds)
    return service
