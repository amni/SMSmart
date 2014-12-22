# SMSmart Multi Input Text Messaging Documentation

This document  details the new input schema we are using. This input schema allows for a client to send a query that spans the length of more than one text message. The only change with this new input schema is that a header is appended to the beginning of each text message. 

#### Header 
The header is comprised of:
- key
- (message number / total number of messages) 

For example, a request that spans 3 text messages with key *z* would have the request headers:
- z(1/3)
- z(2/3)
- z(3/3)

The server will reconstruct the full query once all the messages have arrived.  

For most cases, client requests will not need multiple text messages. However, these singular text message request still need to adhere to the new schema. Fortunately, the change is simple:

**Before**: ```@Yelp search: longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1```

**After**: ```z(1/1) @Yelp search: longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1```



#### Examples:

#####Yelp 
- **Old Schema**: ```@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1```
- **New Schema**: ```z(1/2) @Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: ``` | ```z(2/2) Pizza key: z limit: 1```


#####Maps 
- **Old Schema**: ```@Maps directions: from: san jose, CA to: san francisco, CA key: qw```
- **New Schema**: ```qw(1/2) @Maps directions: from: san jose,``` | ```qw(2/2) CA to: san francisco, CA key: qw```

#####Wikipedia
- **Old Schema**: ```@ Wikipedia summary: search: cars limit: 5 key: z```
- **New Schema**: ```z(1/2) @ Wikipedia summary: search:``` | ```z(2/2) cars limit: 5 key: z```

### Version 0.1
*last updated 12/21/14*