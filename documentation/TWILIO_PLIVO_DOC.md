# Twilio / Plivo Documentation

This documentation describes how to change SMS providers from Twilio to Plivo (or visa versa). All of the changes are made in *app.py*. 

##### Twilio
1) Imports 
```
from twilio.rest import TwilioRestClient 
import twilio.twiml 
```
2) Variable Declarations
```
account_sid = "AC171ca34ca45bf15bb3f369b1ae5e9a9f"
auth_token = "1d3ef112c1407035c6c6f5e5e17f75ad"
client = TwilioRestClient(account_sid, auth_token)
PHONE_NUMBERS = ["+15738182146", "+19738280148", "+16503534855", "+18704740576", "+18702802312"]
```
3) *receive_messages* method
```
def receive_message(): 
    user_text_message = request.values.get('Body')
    phone_number = request.values.get('From')
```
4) *distribute* method
```
def distribute(phone_number, messages_list, key):
    for message in messages_list:
        message = "".join([key, message])
        message.encode('utf-8', 'ignore')
        client.messages.create(to=phone_number, from_=get_phone_number(), body=message)
```
##### Plivo
1) Imports 
```
import plivo, plivoxml
```
2) Variable Declarations
```
auth_id = "MAMJHJZDHJYZBJNJM1MZ"
auth_token = "ODMxYTkzOWRhZmQ0ODZkZmQyYzQyNjAzMmU0NmE2"
p = plivo.RestAPI(auth_id, auth_token)
PHONE_NUMBERS = ["+14159856984", "+19195848629", "+14082143089", "+15733093911", "+15852285686"]
```
3) *receive_messages* method
```
def receive_message(): 
    user_text_message = request.values.get('Text')
    phone_number = request.values.get('From')
```
4) *distribute* method
```
def distribute(phone_number, messages_list, key):
    for message in messages_list:
        message = "".join([key, message])
        message = remove_non_ascii(message)
        message.encode('utf-8', 'ignore')
        params = {
            'src': get_phone_number(), 
            'dst' : phone_number, 
            'text' : message
        }
        p.send_message(params)
```
5) Add *remove_non_ascii* method
```
def remove_non_ascii(s): 
    return "".join(i for i in s if ord(i)<128)
```

### Version 0.1
*last updated 01/30/15*