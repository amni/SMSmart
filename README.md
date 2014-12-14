SMSmart
=======

All of Your Favorite Applications, None of Data


Structure:

The backend is where our backend server lives.  This contains all of the Twilio code and Api interfacing.  The code that is live here serves as the gateway for SMS messages from users and also sends SMS messages to users.  

The frontend directory contains our landing page and all of the data needed for our landing page.  This includes interfacing with our Firebase data store and all the html, css, and javascript used to make the landing page.  

Deployment:

To run the following project, you must 

1. Install pip
2. In the backend directory run, pip install -r requirements.txt
3. In the backend directory run python app.py


To send a text message to our server, please text 973 828 0148. 

Limitations:

Current limitations to our service are that text messages that are served from this number are not in a highly readable form. To use our application, users are expected to download the Android application.  

