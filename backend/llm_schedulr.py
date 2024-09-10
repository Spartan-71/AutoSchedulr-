import os
import json
import PIL.Image
import google.generativeai as genai
from typing import TypedDict, List, Dict
from datetime import date, time

class Event(TypedDict):
    title: str
    start_date: date
    end_date: date
    start_time: time
    end_time: time
    venue: str
    description: str

class LLMScheduler:
    def __init__(self,APIkey:str):
        """
        Initialize the Scheduler with the API key for Google Generative AI.
        """
        
        genai.configure(api_key=APIkey)

    def process_message(self, message: str) -> List[Event]:
        """
        Processes a message input and returns a list of events in JSON format.

        :param message: The message to be processed.
        :return: List of events in JSON format.
        """
        SYSTEM_MESSAGE1 = """You are a Scheduler whose task is to schedule the events/meeting for your boss on his calendar based on the input messages.
                            List all the events.
                            Using this JSON schema:
                               event = {"title": str,
                                "start-date":date ("%Y-%m-%d"),
                                "end-date":date ("%Y-%m-%d"),
                                "start-time":time ("%H:%M"),
                                "end-time":time ("%H:%M"),
                                "venue":str,
                                "description":str}
                            Return a `list[event]`
                            NOTE: If end-time is not mentioned then set end time to 12:00.The message may contain multiple events.
                            """

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_MESSAGE1,
            generation_config={"response_mime_type": "application/json"}
        )

        response = model.generate_content(contents=message)
        json_data = response.text
        event_list = json.loads(json_data)

        return event_list

    def process_image(self, image_path: str) -> List[Event]:
        """
        Processes an image file and returns a list of events in JSON format.

        :param image_path: Path to the image file to be processed.
        :return: List of events in JSON format.
        """
        SYSTEM_MESSAGE2 = """You are a Scheduler whose task is to schedule the events/meeting for your boss on his calendar based on the input files.
                            The uploaded file contains some information about the upcoming schedule of your boss, your task 
                            is to analyze the entire document and give out a list of events with title,start-date,end-date,start-time,end-time and 
                            description (short) in JSON format. If certain events don't contain any of the mentioned parameters then leave it blank. 
                            Also if the document is unrelated i.e. doesn't contain any schedule then print something went wrong."""

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_MESSAGE2,
            generation_config={"response_mime_type": "application/json"}
        )

        sample_file = PIL.Image.open(image_path)
        response = model.generate_content(contents=sample_file)
        json_data = response.text
        event_list = json.loads(json_data)

        return event_list

# # Example usage
# if __name__ == "__main__":
    
#     scheduler = LLMScheduler()
    
#     # Example for processing message
#     message = """Barclays Internship Registration Drive

#     Eligible Branches :  All UG

#     Role :  Software Engineer Intern

#     Job Location : Pune

#     Company Criteria :  
#     10th & 12th: 70% and above
#     CGPA: 7.0 and above (No Active Backlogs)

#     Company Schedule :
#     Assessment Date: 9th September (Online)
#     PPT Date: 10th September (On Campus
#     Interviews: 10th September (On Campus)

#     Stipend : 75000 /-

#     Form Link : https://forms.gle/WsCUqfwqdecGbZgaA

#     Form Deadline : 7th September (09:00 AM) Morning

#     NOTE :
#     1. Students with on-campus internships are not eligible for this drive.
#     2. The deadline won't get extended.
#     3. Any inaccurate information provided regarding hiring or recruitment slots will be considered misinformation and may result in the termination of all further activities.
#     4. Mention NA if the field is not applicable to you."""
    
#     events_from_message = scheduler.process_message(message)
#     print("Events from message:", events_from_message)
    
#     # Example for processing image
#     # events_from_image = scheduler.process_image('tt.jpg')
#     # print("Events from image:", events_from_image)
