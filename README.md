SMSmart
=======
*All of Your Favorite Applications, None of Data*

###Welcome to the Backend!
Here is where out server lives.  This contains all of the Twilio code and Api interfacing. The code that is live here serves as the gateway for SMS messages from users and also sends SMS messages to users. To learn more about SMSmart, please visit our website at - http://www.getsmsmart.com/.   

##### Getting Started
To run the following project, you must first: 
- 1. Install pip
- 2. In the backend directory run, pip install -r requirements.txt
- 3. In the backend directory run python app.py

##### Phone Numbers
Twilio Numbers:
- +15738182146 (**production server endpoint**)
- +19738280148 (**testing server endpoint**)
- +16503534855
- +18704740576
- +18702802312

Plivo Numbers:
- +14159856984 (**plivo server endpoint**)
- +19195848629
- +14082143089
- +15733093911
- +15852285686

#####Technology Stack
Currently, we are using the following:
- Flask Web App - Python web framework (http://flask.pocoo.org/)
- MongoDB - open source document database (http://www.mongodb.org/)
- Mongoengine - Python object data mapper for MongoDB (http://mongoengine.org/) 
- Heroku - cloud platform as a service for web hosting (https://www.heroku.com/) 

#####Limitations
Current limitations to our service are that text messages that are served from this number are not in a highly readable form. To use our application, users are expected to download the Android application.  
