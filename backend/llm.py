import sys
import os
import json
import PIL.Image
import google.generativeai as genai
from typing import TypedDict
from datetime import date, time

genai.configure(api_key=os.environ["API_KEY"])

class Event(TypedDict):
    title: str
    start_date: date
    end_date: date
    start_time: time
    end_time: time
    venue: str
    description: str


# Parsing the messages
SYSTEM_MESSAGE1 = """You are a Scheduler whoes task is to schedule the events/meeting for your boss on his calendar based on the input messages.
                    List all the events.
                    Using this JSON schema:
                       event = {"title": str,
                        "start-date":date,
                        "end-date":date,
                        "start-time":time,
                        "end-time":time,
                        "venue":str,
                        "description":str}
                    Return a `list[event]`
                    NOTE: If any of the following field is missing just leave it empty.The message may contain multiple events.
                    Datatype of the response must be list of json objects."""
USER_QUESTION = """Barclays Internship Registration Drive

        Eligible Branches :  All UG

        Role :  Software Engineer Intern

        Job Location : Pune

        Company Criteria :  
        10th & 12th: 70% and above
        CGPA: 7.0 and above (No Active Backlogs)

        Company Schedule :
        Assessment Date: 9th September (Online)
        PPT Date: 10th September (On Campus
        Interviews: 10th September (On Campus)

        Stipend : 75000 /-

        Form Link : https://forms.gle/WsCUqfwqdecGbZgaA

        Form Deadline : 7th September (09:00 AM) Morning

        NOTE :
        1. Students with on-campus internships are not eligible for this drive.
        2. The deadline won't get extended.
        3. Any inaccurate information provided regarding hiring or recruitment slots will be considered misinformation and may result in the termination of all further activities.
        4. Mention NA if the field is not applicable to you."""

model1 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_MESSAGE1,
    generation_config={"response_mime_type": "application/json"})

response = model1.generate_content(contents=USER_QUESTION)
json_data = response.text
# converting json string to json object by parsing
json_data = json.loads(json_data)

print(f"datatype: {type(json_data)}")

with open('events.json', 'w') as json_file:
    json.dump(json_data, json_file)

# for item in json_data:  
#     title = item["title"]
#     start_date = item["start-date"]
#     end_date = item["end-date"]
#     start_time = item["start-time"]
#     end_time = item["end-time"]
#     venue= item["venue"]
#     description = item["description"]
    
#     print(f"Title: {title}")
#     print(f"Start Date: {start_date}")
#     print(f"End Date: {end_date}")
#     print(f"Start Time: {start_time}")
#     print(f"End Time: {end_time}")
#     print(f"Venue: {venue}")
#     print(f"Description: {description}")
#     print("---")



# Processing the images (<20MB)
SYSTEM_MESSAGE2="""You are a Scheduler whoes task is to schedule the events/meeting for your boss on his calendar based on the input files.
                The uploaded file containes some information about the upcoming schedule of your boss, your task 
                is to analyse the entire document and give out a list of events with title,start-date,end-date,start-time,end-time and 
                description (short) in json format. If certain events doesn't contain any of the mentioned parameters then leave it blank. 
                Also if the document is not unrelated i.e doesn't contain any schedule then print something went wrong."""

model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_MESSAGE2,
    generation_config={"response_mime_type": "application/json"})

sample_file = PIL.Image.open('tt.jpg')
response = model2.generate_content(contents=sample_file)

print(response.text)        
