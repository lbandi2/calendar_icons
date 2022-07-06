from icons import Calendar
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_API')
CAL_ID = os.getenv('CALENDAR_ID')

Calendar(CAL_ID, API_KEY)
