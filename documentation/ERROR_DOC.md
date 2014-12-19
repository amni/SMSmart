# SMSmart Error Messaging Documentation
Error codes will be added to the beginning of every text message (before the key). For the time being, error codes will only take up one character [0-9]. 
##### 1) Yelp  
**Programs:** 
- search (*default*)

**Error Codes:**
- 0 - success
- 1 - SMSmart / API Error

**Examples:** 
```
Text - '@Yelp: near: ff3e21 category: 2312ds key: z'
Response - '1z(1/1)* '
```


##### 2) Maps  
**Programs:**
- directions (*default*)

**Error Codes:**
- 0 - success
- 1 - API Error
- 2 - SMSMart / Other Error 

**Examples:**
```
Text - '@ maps directions : key: d  to: fdsfs231  from: fdsf13 mode: driving'
Response - '1d(1/1)* '
```

##### 3) Wikipedia
**Programs:**
- search (*default*)
- summary

**Error Codes** *(currently same codes for both programs)*:
- 0 - success
- 1 - Disambiguation Error
- 2 - Page Error (page does not exist)
- 3 - SMSmart / API Error

**Examples:**
```
Text - '@ Wikipedia summary: term: Mercury limit: 3 key: z'
Response - '1z(1/1)* '
```
```
Text - '@ Wikipedia summary: term: zv#432v* limit: 3 key: z'
Response - '2z(1/1)* '
```

### Version 0.1
*last updated 12/18/14*

