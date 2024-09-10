from gcsa.google_calendar import GoogleCalendar
from beautiful_date import Sept, hours
from gcsa.event import Event
from gcsa.reminders import PopupReminder
from datetime import datetime
import json

gc = GoogleCalendar('anishdabhane@gmail.com')


with open('events.json', 'r') as json_file:
    eve_list = json.load(json_file)

print(eve_list)  

for eve in eve_list:
    name = eve["title"]
    desc= eve["description"]
    venue = eve["venue"]

    start_date=eve["start-date"]
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    
    start_time = eve["start-time"]
    start_time_obj = datetime.strptime(start_time, "%H:%M").time()

    start_datetime_obj = datetime.combine(start_date_obj, start_time_obj)
    start = start_datetime_obj

    end_date=eve["end-date"]
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    
    end_time = eve["end-time"]
    end_time_obj = datetime.strptime(end_time, "%H:%M").time()

    end_datetime_obj = datetime.combine(end_date_obj, end_time_obj)
    end = end_datetime_obj

    # print(f"Start {start}")
    # print(f"END {end}")
    # print(f"dtype{type(start)}")

    event = Event(name,
                start=start_datetime_obj,
                end=end_datetime_obj,
                description=desc,
                location=venue,
                reminders=[
                    PopupReminder(minutes_before_start=60),
                    PopupReminder(minutes_before_start=30),
                    PopupReminder(minutes_before_start=15)
              ])

    event = gc.add_event(event)

