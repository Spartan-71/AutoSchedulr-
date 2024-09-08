import google.generativeai as genai
import PIL.Image
import os
from typing import TypedDict
import json
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
USER_QUESTION = """Greetings everyone! ✨

As we know, selecting an appropriate theme for the college's annual magazine is one of the important steps in the curation process. ✨

Let us begin the journey of crafting Xenia Volume 27 by deciding a suitable theme for our upcoming masterpiece! Put forth your ideas regarding the theme for college magazine's 27th volume! 📚🎨

If you have any questions or need further details, feel free to reach out to any of us!
Shruti Mone: +91 96234 58658
Amulya Agrawal: +91 88303 21661

Form link: https://forms.gle/fCKefRrUap5Je7KD9

Deadline to fill: 21st September, 2024

Note:
1. The form is open for everyone including faculty members, not just Xenia members.
2. This form will take 5-10 minutes to go through it. READ THE FORM COMPLETELY BEFORE PROCEEDING TO FILL IT.
3. Refer the form description for expected format of theme title and description to be submitted."""

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
# SYSTEM_MESSAGE2="""You are a Scheduler whoes task is to schedule the events/meeting for your boss on his calendar based on the input files.
#                 The uploaded file containes some information about the upcoming schedule of your boss, your task 
#                 is to analyse the entire document and give out a list of events with title,start-date,end-date,start-time,end-time and 
#         SYSTEM_MESSAGE2="""You are a Scheduler whoes task is to schedule the events/meeting for your boss on his calendar based on the input files.
#                 The uploaded file containes some information about the upcoming schedule of your boss, your task 
#                 is to analyse the entire document and give out a list of events with title,start-date,end-date,start-time,end-time and 
#                 description (short) in json format. If certain events doesn't contain any of the mentioned parameters then leave it blank. 
#                 Also if the document is not unrelated i.e doesn't contain any schedule then print something went wrong."""

# model2 = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     system_instruction=SYSTEM_MESSAGE2,
#     generation_config={"response_mime_type": "application/json"})

# sample_file = PIL.Image.open('tt.jpg')
# response = model2.generate_content(contents=sample_file)

# print(response.text)        description (short) in json format. If certain events doesn't contain any of the mentioned parameters then leave it blank. 
#                 Also if the document is not unrelated i.e doesn't contain any schedule then print something went wrong."""

# model2 = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     system_instruction=SYSTEM_MESSAGE2)

# sample_file = PIL.Image.open('tt.jpg')
# response = model2.generate_content(contents=sample_file)

# print(response.text)