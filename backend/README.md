# SMSmart Text Messaging Documentation

##### 1) Yelp  
**Programs:** 
- search (*default*)

**Parameters:**
- key (*required*)
- longlat
- near
- category
- limit

**Examples: ** 
```
Text - '@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1'
Response - 'z^1|NY Pizza Suprema (Pizza)|413 8th Ave, New York, NY 10001|(212) 594-8939|4.0 stars|open'
```
```
Text - '@Yelp: near: Durham, NC category: bars key: z'
Response - 'z^1|Alley Twenty Six (Lounges)|320 E Chapel Hill St, Durham, NC 27701|(919) 213-1267|4.5 stars|open^2|Fullsteam Brewery (Breweries)|726 Rigsbee Ave, Durham, NC 27701|(919) 682-2337|4.5 stars|open^3|The Green Room (Pool Halls)|1108 Broad St, Durham, NC 27705|(919) 286-2359|4.5 stars|open^4|Surf Club (Bars)|703 Rigsbee Ave, Durham, NC 27701|(919) 294-9661|4.5 stars|open^5|Dains Place (American (Traditional))|754 9th St, Durham, NC 27705|(919) 416-8800|4.0 stars|open^6|Motorco Music Hall (Bars)|723 Rigsbee Ave, Durham, NC 27701|(919) 901-0875|4.0 stars|open'
```



##### 2) Maps  
**Programs:**
- directions (default)

**Parameters:**
- key (*required*)
- from
- to
- mode (*default = "driving"*)

**Examples:**
```
Text - '@Maps directions: from: san jose, CA to: san francisco, CA key: z'
Response - 'z^1|Head south on S Market St toward Park Ave|0.1 mi^2|Turn right onto Park Ave|0.3 mi^3|Turn right onto the California 87 N ramp|0.1 mi^4|Merge onto CA-87 N|3.4 mi^5|Take the US-101 N exit on the left toward San Francisco|0.2 mi^6|Keep left, follow signs for US 101 N/San Francisco and merge onto US-101 N|42.8 mi^7|Keep left to stay on US-101 N|0.8 mi^8|Continue onto Central Fwy|0.4 mi^9|Turn right onto Market St|0.3 mi'
```
```
Text - '@Maps directions: from: chapel hill, NC to: Durham, NC key: z mode: walking'
Response - 'z^1|Head southeast on N Columbia St toward W Franklin St|30 ft^2|Turn left onto E Franklin St|2.4 mi^3|Slight right to stay on E Franklin St|0.3 mi^4|Slight left onto Dobbins Dr|0.9 mi^5|Turn right onto Sage Rd|118 ft^6|Continue onto Scarlett Dr|210 ft^7|Slight left onto Old Durham Rd|0.5 mi^8|Continue onto Durham Rd|276 ft^9|Continue onto Old Chapel Hill Rd|0.5 mi^10|Slight right to stay on Old Chapel Hill Rd|210 ft^11|At the traffic circle, continue straight to stay on Old Chapel Hill Rd|0.5 mi^12|Slight left to stay on Old Chapel Hill Rd|0.7 mi^13|Slight right to stay on Old Chapel Hill Rd|0.6 mi^14|Continue onto University Dr|4.5 mi^15|Continue onto US-15 BUS N/US-501 BUS N/W Lakewood Ave|0.4 mi^16|Turn left onto US-15 BUS N/US-501 BUS N/S Roxboro St|0.4 mi^17|Turn left onto E Main StDestination will be on the right|112 ft'
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
Text - '@ Wikipedia search: term: Ford limit: 3 key: z'
Response - 'z^Car^A car is a wheeled, self-powered motor vehicle used for transportation. Most definitions of the term specify that cars are designed to run primarily on roads, to have seating for one to eight people, to typically have four wheels, and to be constructed principally for the transport of people rather than goods. The year 1886 is regarded as the birth year of the modern car. In that year, German inventor Karl Benz built the Benz Patent-Motorwagen. Cars did not become widely available until the early 20th century.'
```
```
Text - '@ Wikipedia summary: search: cars limit: 5 key: z'
Response - 'z^Ford Motor Company^Gerald Ford^List of Ford vehicles'
```
### Version 0.1 
*last updated 12/14/14*


