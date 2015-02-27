# SMSmart Internationalization Documentation

#####Plivo Numbers:  
US Numbers = ["+14159856984", "+19195848629", "+14082143089", "+15733093911", "+15852285686"]  
UK Numbers = ["+447441906017", "+447441906514", "+447441906376", "+447441906383", "+447441906394"]    
CA Numbers = ["+12894320286", "+15813183824", "+14184781054", "+15877824197", "+12893520921"]  

##### Mappings:
Code: `PHONE_NUMBERS = {'US':PHONE_NUMBERS_US, 'UK': PHONE_NUMBERS_UK, 'CA': PHONE_NUMBERS_CA}`

United States - `US`  
United Kingdom - `UK`  
Canada - `CA`  

For new countries, follow the 2 letter abbreviations at: http://www.worldatlas.com/aatlas/ctycodes.htm. 

##### Message Interface:
Include the country field with the corresponding country abbrevation. 

**Sample Request Message**:  
@Yelp: near: Durham, NC category: bars key: z **c: CA**


### Version 0.1 
*last updated 02/26/15*
