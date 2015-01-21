# SMSmart Text Messaging Documentation

##### 0) Onboard
Client generated input request for Onboard is: ```@Onboard```. Server will send texts containing our custom response to the client's phone number from each of SMSmart's phone numbers (currently there are 5). 

**Returns**
Boolean||Message

**Examples:** 
```
Text - '@Onboard'
Response - 'T||Welcome to SMSmart. Please blacklist this number for the best experience'
```


##### 1) Yelp  
**Programs:** 
- search (*default*)

**Parameters:**
- key (*required*)
- longlat
- near
- category
- limit

**Examples:** 
```
Text - '@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1'
Response - '0z^^1||NY Pizza Suprema (Pizza)||413 8th Ave, New York, NY 10001||(212) 594-8939||4.0 stars||open'
```
```
Text - '@Yelp: near: Durham, NC category: bars key: z'
Response - '0z^^1||Alley Twenty Six (Lounges)||320 E Chapel Hill St, Durham, NC 27701||(919) 213-1267||4.5 stars||open^^2||Fullsteam Brewery (Breweries)||726 Rigsbee Ave, Durham, NC 27701||(919) 682-2337||4.5 stars||open^^3||The Green Room (Pool Halls)||1108 Broad St, Durham, NC 27705||(919) 286-2359||4.5 stars||open^^4||Surf Club (Bars)||703 Rigsbee Ave, Durham, NC 27701||(919) 294-9661||4.5 stars||open^^5||Dains Place (American (Traditional))||754 9th St, Durham, NC 27705||(919) 416-8800||4.0 stars||open^^6||Motorco Music Hall (Bars)||723 Rigsbee Ave, Durham, NC 27701||(919) 901-0875||4.0 stars||open'
```



##### 2) Maps  
**Programs:**
- directions (default)

**Parameters:**
- key (*required*)
- from
- to
- mode (*default = 'driving'*)
- geo (*default = 'F'*)

**Examples:**
```
Text - '@Maps directions: from: san jose, CA to: san francisco, CA key: zo'
Response - '0z^^1||Head south on S Market St toward Park Ave||0.1 mi^^2||Turn right onto Park Ave||0.3 mi^^3||Turn right onto the California 87 N ramp||0.1 mi^^4||Merge onto CA-87 N||3.4 mi^^5||Take the US-101 N exit on the left toward San Francisco||0.2 mi^^6||Keep left, follow signs for US 101 N/San Francisco and merge onto US-101 N||42.8 mi^^7||Keep left to stay on US-101 N||0.8 mi^^8||Continue onto Central Fwy||0.4 mi^^9||Turn right onto Market St||0.3 mi'
```
```
Text - '@Maps directions: from: chapel hill, NC to: Durham, NC key: z mode: walking'
Response - '0z^^1||Head southeast on N Columbia St toward W Franklin St||30 ft^^2||Turn left onto E Franklin St||2.4 mi^^3||Slight right to stay on E Franklin St||0.3 mi^^4||Slight left onto Dobbins Dr||0.9 mi^^5||Turn right onto Sage Rd||118 ft^^6||Continue onto Scarlett Dr||210 ft^^7||Slight left onto Old Durham Rd||0.5 mi^^8||Continue onto Durham Rd||276 ft^^9||Continue onto Old Chapel Hill Rd||0.5 mi^^10||Slight right to stay on Old Chapel Hill Rd||210 ft^^11||At the traffic circle, continue straight to stay on Old Chapel Hill Rd||0.5 mi^^12||Slight left to stay on Old Chapel Hill Rd||0.7 mi^^13||Slight right to stay on Old Chapel Hill Rd||0.6 mi^^14||Continue onto University Dr||4.5 mi^^15||Continue onto US-15 BUS N/US-501 BUS N/W Lakewood Ave||0.4 mi^^16||Turn left onto US-15 BUS N/US-501 BUS N/S Roxboro St||0.4 mi^^17||Turn left onto E Main StDestination will be on the right||112 ft'
```
*Example with geo (lat/lng)*:
```
Text - '@Maps directions : key: e  to: Castro Street, Mountain View, CA  from: 37.253135,-121.904945 mode: driving geo: T'
Response - '0e^^1||Head north on Canberra Ct toward Wyndham Dr||102 ft^^2||Take the 1st right onto Wyndham Dr||0.1 mi^^3||Turn right onto Kirk Rd||295 ft^^4||Turn right onto Branham Ln||0.4 mi^^5||Take the California 85 N ramp on the left||0.2 mi^^6||Merge onto CA-85 N||13.6 mi^^7||Exit onto CA-82 N/E El Camino Real toward Mountain View||1.2 mi^^8||Turn right onto Castro St||0.2mi#1||37.2534045,-121.9052406^^2||37.2539644,-121.9030174^^3||37.2532013,-121.9026889^^4||37.2512019,-121.9104474^^5||37.2507045,-121.9135202^^6||37.378277,-122.0675624^^7||37.3857917,-122.0838069^^8||37.3883427,-122.0823537'
```
##### 3) Wikipedia
**Programs:**
- search (*default*)
- summary
- random (*to be implemented*)

**Parameters:**
- key (*required*)
- term
- limit (*default = 5 for search, default = 3 for summary*)

**Examples:**
```
Text - '@ Wikipedia summary: term: Ford limit: 3 key: z'
Response - '0z^^Car||A car is a wheeled, self-powered motor vehicle used for transportation. Most definitions of the term specify that cars are designed to run primarily on roads, to have seating for one to eight people, to typically have four wheels, and to be constructed principally for the transport of people rather than goods. The year 1886 is regarded as the birth year of the modern car. In that year, German inventor Karl Benz built the Benz Patent-Motorwagen. Cars did not become widely available until the early 20th century.'
```
```
Text - '@ Wikipedia search: term: cars limit: 5 key: z'
Response - '0z^^Ford Motor Company^^Gerald Ford^^List of Ford vehicles'
```

##### 4) Sending Post Requests
**Parameters:**
- Body - User Query
- From - User Phone Number 
- Wifi - Include a true boolean

**Response:**
```
{"results": "0a^^Cat^^The domestic cat (Felis catus or Felis silvestris catus) is a small, usually furry, domesticated, and carnivorous mammal. It is often called a housecat when kept as an indoor pet, or simply a cat when there is no need to distinguish it from other felids and felines. Cats are often valued by humans for companionship, and their ability to hunt vermin and household pests."}
```

##### 5) User using over limit of text messsages

**Response:**
```
{"results": "text_limit: 30"} //(number of text messages a user is allotted under current plan) 
```
##### 6) Search
**Programs:**
- query

**Parameters:**
- key (*required*)
- term (*required*) 

**Examples:**
```
Text - '@ news feed: key: z'
Response - '(1/5)*Several gunshots fired from vehicle passing Vice President Biden's Delaware home Saturday night ^^5 Belgian nationals charged with participation in ter'
```
##### 7) News
**Programs:**
- feed

**Parameters:**
- key (*required*)

**Returns**
- title||details 

**Examples:**
```
Text - '@ search query: term: android key: a'
Response - '(1/6)*Android||Official site provides information for users, developers and partners. Includes press releases, videos, screenshots and downloads.^^Android (op', u'(2/6)*erating system) - Wikipedia, the free encyclopedia||Android is a mobile operating system (OS) based on the Linux kernel and currently developed by Goog','
```

##### 8) Weather 
**Programs:**
- search

**Parameters:**
- key (*required*)
- near (*required*) 

**Examples:**
```
Text - @ weather search: near: london,uk key: a'
Response - '(1/1)*london,uk||clear||32.54'
```
##### 9) Stock
**Programs:**
- search

**Parameters:**
- key (*required*)
- symbol (*required*)

**Returns**
- stocksymbol||current price||starting price 

**Examples:**
```
Text - '@ stock search: symbol: goog key: a'
Response - '(1/1)*goog||508.08||500.00'
```

### Version 0.7
*last updated 01/18/15*


