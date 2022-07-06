import emoji
import json
import random
import re
from events import get_events, update_cal_event

with open('./categories.json') as f:
    CATEGORIES = json.load(f)

class Calendar:
    def __init__(self, cal_id, api_key):
        self.cal_id = cal_id
        self.api_key = api_key
        self.events = get_events(self.cal_id)
        self.check_all_events()

    def fetch_events(self):
        events = get_events(self.cal_id)
        return events

    def has_description(self, event):
        if 'description' in event:
            return True
        return False

    def has_icon(self, event):
        if self.has_description(event):
            if 'icon: true' in event['description']:
                return True
        return False

    def get_icon(self, event):
        title = event['summary']
        for unused, categ in CATEGORIES.items():
            for item in categ:
                words = item['string']
                icons = item['icon']
                for word in words:
                    if word in title.lower():
                        icon = random.choice(icons).replace(" ", "_")
                        return icon
        return None

    def get_text(self, event):
        title = event['summary']
        for item in CATEGORIES.items():
            text = item[1][0]['string']
            for word in text:
                if word in title.lower():
                    return word
        return None

    def check_all_events(self):
        for event in self.events:
            title = event['summary']
            if not self.has_icon(event):
                icon = self.get_icon(event)
                if icon is not None:
                    text = self.get_text(event)
                    self.update_event(event, text, icon)
                else:
                    print(f'No icon found for {title.encode("utf-8")}')
            else:
                # print(f'Skipping {title.encode("utf-8")}')
                print(f'Skipping {emoji.demojize(title)}')

    def set_description(self, event, old_title):
        title = event['summary']
        if self.has_description(event):
            event['description'] += f"\n"
        else:
            event['description'] = ""
        if not self.has_icon(event):
            event['description'] += f"icon: true\n"
        if old_title is not None:
            if title != old_title:
                event['description'] += f"old_title: {old_title}"

    def cleanup_title(self, event):
        title = event['summary']
        if bool(re.match('^\w+:', title)):  ## remove tag string if found
            tag_string = re.match('^\w+:', title).group()
            print(tag_string)
            title = title.replace(tag_string, '').lstrip(' ')
        return title

    def update_event(self, event, text, icon):
        old_title = event['summary']
        title = self.cleanup_title(event)
        self.set_description(event, old_title)
        emoji_icon = emoji.emojize(f':{icon}:')
        print(f"Adding emoji to {title}")
        event['summary'] = f"{emoji_icon} {title}"
        update_cal_event(self.cal_id, event['id'], event)
