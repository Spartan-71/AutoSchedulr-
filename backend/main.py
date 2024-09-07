from gcsa.google_calendar import GoogleCalendar

calendar = GoogleCalendar('anishdabhane@gmail.com')
for event in calendar:
    print(event)