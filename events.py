from datetime import datetime
from cal_setup import get_calendar_service

def get_events(calendar_id):
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.utcnow().replace(hour=0, minute=0).isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting List of all events')
    events_result = service.events().list(
        calendarId=calendar_id, timeMin=now,
        singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events

def update_cal_event(calendar_id, event_id, dict):
    service = get_calendar_service()
    try:
        response = service.events().update(calendarId=calendar_id, eventId=event_id, body=dict).execute()
        return response
    except Exception as e:
        return e.message