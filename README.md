# AutoSchedulr

![banner](https://github.com/user-attachments/assets/f429c1e7-03db-42af-9507-67edb47e17c0)

Auto Schedulr is a Python-based web application built to streamline your scheduling process by automating the addition of events to your Google Calendar. Sync your timetable effortlessly with Google Calendar for classes, meetings, or appointments.

## Key Features

- **Automated Event Creation**: Automatically add events to Google Calendar based on a timetable input.
- **Google Calendar Integration**: Seamless syncing of events using the Google Calendar API.
- **Timetable Input**: Input your schedule manually or upload it in a compatible format.
- **Custom Event Settings**: Customize event details like reminders and durations.
- **Streamlit Interface**: A simple and responsive UI built using Streamlit.


## Architecture
![architecture diagram](https://github.com/user-attachments/assets/9a516c08-9cd4-442b-a196-6cc51af6bf14)


## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/auto-schedulr.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Google Calendar API**:
   - Create a project on [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Calendar API.
   - Set up OAuth 2.0 credentials and download the credentials file.
   - Add the credentials file to the project directory.
     
4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---
