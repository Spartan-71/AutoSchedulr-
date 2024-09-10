from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
from gcsa.reminders import PopupReminder
from datetime import datetime
import json

class CalendarScheduler:
    def __init__(self,Credentials):
        """
        Initialize the CalendarScheduler with a Google Calendar for the given email.
        """
        self.calendar = GoogleCalendar(credentials=Credentials,save_token=False)

    def create_event(self, event_data: dict) -> Event:
        """
        Create an Event object from the event data.

        :param event_data: A dictionary containing event details.
        :return: An Event object.
        """
        name = event_data.get("title", "Untitled Event")
        description = event_data.get("description", "")
        venue = event_data.get("venue", "")

        # Parse start date and time
        start_date_str = event_data.get("start-date", "")
        start_time_str = event_data.get("start-time", "")
        start_datetime_obj = self.parse_datetime(start_date_str, start_time_str)

        # Parse end date and time
        end_date_str = event_data.get("end-date", "")
        end_time_str = event_data.get("end-time", "")
        end_datetime_obj = self.parse_datetime(end_date_str, end_time_str)

        # Create event
        event = Event(
            name,
            start=start_datetime_obj,
            end=end_datetime_obj,
            description=description,
            location=venue,
            reminders=[
                PopupReminder(minutes_before_start=60),
                PopupReminder(minutes_before_start=30),
                PopupReminder(minutes_before_start=15)
            ]
        )
        return event

    def parse_datetime(self, date_str: str, time_str: str) -> datetime:
        """
        Parse the date and time strings into a datetime object.

        :param date_str: Date string in 'YYYY-MM-DD' format.
        :param time_str: Time string in 'HH:MM' format.
        :return: A combined datetime object.
        """
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        return datetime.combine(date_obj, time_obj)

    def add_events_to_calendar(self, event_list: list[Event]):
        """
        Add a list of events to the Google Calendar.

        :param event_list: A list of event dictionaries.
        """
        for event_data in event_list:
            print(f"event data {event_data}")
            print(f"datatype {type(event_data)}")
            event = self.create_event(event_data)
            self.calendar.add_event(event)
            print(f"Added event: {event.summary}")

# Example usage
# if __name__ == "__main__":
#     # Initialize the scheduler with your email
#     scheduler = CalendarScheduler('anishdabhane@gmail.com')

#     # Load events from a JSON file
#     events = scheduler.load_events('events.json')

#     # Add events to Google Calendar
#     scheduler.add_events_to_calendar(events)



