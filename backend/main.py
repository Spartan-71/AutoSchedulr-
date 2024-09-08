from gcsa.google_calendar import GoogleCalendar
from beautiful_date import Sept, hours
from gcsa.event import Event
import json

gc = GoogleCalendar('anishdabhane@gmail.com')


with open('events.json', 'r') as json_file:
    eve_list = json.load(json_file)

print(eve_list)  

for eve in eve_list:
    name = eve["title"]
    desc= eve["description"]
    venue = eve["venue"]
    start = (19/Sept/2024)[2:00]
    end = start +  10* hours
    event = Event(name,
                start=start,
                end=end,
                description=desc,
                venue=venue)

    event = gc.add_event(event)

