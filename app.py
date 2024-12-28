import os
import time
import streamlit as st
from backend.llm_schedulr import LLMScheduler
from backend.google_schedulr import CalendarScheduler
from audio_recorder_streamlit import audio_recorder

# Using "with" notation
with st.sidebar:
    st.markdown("#### Gmail")
    title = st.text_input("Enter your Gmail address")

    st.divider()

    # with st.expander("**How to Use ?**"):
    #     st.write("slkdjaksjdlks skdlksl;d")
    with st.expander("Socials"):
        st.link_button("Github", "https://github.com/Spartan-71/Schedulr",use_container_width=True)
        st.link_button("Twitter", "https://x.com/AnishDabhane",use_container_width=True)
    
    with st.expander("**Feedback**"):
        st.text_area(label="feedback",label_visibility="collapsed")
        if st.button("SUBMIT"):
            st.write("Thanks")

    st.markdown("#### RATE US")
    selected = st.feedback('stars')
    if selected is not None:
        st.write("Thank You :)")



# @st.dialog("SignIN/SignUp")
# def authentication():
#     st.markdown("##### Name")
#     name = st.text_input(label="Name",label_visibility="collapsed")
#     st.markdown("##### Gmail_ID")
#     gmail_id= st.text_input(label="Gmail",label_visibility="collapsed")
    
#     if st.button("Submit"):
#         st.rerun()

# # if st.session_state:
# #     authentication()


# llm_obj= LLMScheduler(APIkey=st.secrets["API_KEY"])
llm_obj= LLMScheduler(APIkey=os.environ["GEMINI_API_KEY"])
# cal_obj = CalendarScheduler(Credentials=st.secrets["GOOGLE_CREDENTIALS"])
# cal_obj = CalendarScheduler()
review = 1

st.logo("logo.png")

st.title("Schedulr")
st.write("A Multimodal AI Agent automates adding events, tasks, and reminders to Google Calendar.")
st.divider()

st.markdown("#### Paste/Enter a Message")
msg = st.text_area(label="Enter message here",label_visibility="collapsed")

if st.button("Submit") and msg:

    msg_event_list = llm_obj.process_message(msg)
    st.write_stream(msg_event_list)
    if msg_event_list:
        # cal_obj.add_events_to_calendar(msg_event_list)
        # progress_text = "Prcoessing..."
        # my_bar = st.progress(0, text=progress_text)

        # for percent_complete in range(100):
        #     time.sleep(0.01)
        #     my_bar.progress(percent_complete + 1, text=progress_text)
        # time.sleep(1)

        st.success('Event added to ur Calendar!', icon="✅")
    else:
        st.error('Error is adding event to Calendar',icon="🚨")
    review = st.feedback('thumbs')

st.divider()

st.markdown("#### Record")

audio_value = st.audio_input("Record a voice message")

st.button("Done")

st.divider()

st.markdown("#### Upload the Image/File")

uploaded_file = st.file_uploader(label="**Upload** an Image/File",label_visibility="collapsed")
# st.warning('File size must be less than 20MB', icon="⚠️")

if st.button("submit") and uploaded_file:
    file_event_list=llm_obj.process_image(uploaded_file)

    if file_event_list:
        # cal_obj.add_events_to_calendar(file_event_list)
        st.success('Event added to ur Calendar!', icon="✅")
    else:
        st.error('Error is adding event to Calendar',icon="🚨")
    review=st.feedback('thumbs')
    


st.divider()
# upvotes=0
# downvotes=0
# if review:
#     upvotes+=1
# else:
#     downvotes+=1

# st.markdown("#### Stats")
# col1, col2, col3 = st.columns(3)
# col1.metric("Events Scheduled", "70","+10")
# col2.metric("Upvotes", upvotes, "+1")
# col3.metric("Downvotes", downvotes, "4")

# st.divider()

# col4,col5 = st.columns(2)
# with col4:
#     st.link_button("Github", "https://github.com/Spartan-71/AutoSchedulr",use_container_width=True)
# with col5:
#     st.link_button("Twitter", "https://x.com/AnishDabhane",use_container_width=True)

