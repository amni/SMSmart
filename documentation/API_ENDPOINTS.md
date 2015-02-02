# SMSmart API Endpoints

##### 1) url(testing or prod)/
**Examples:** 
```
Arguments- {Body: '@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1, From: 5734894023
Response - {results : '1|NY Pizza Suprema (Pizza)|413 8th Ave, New York, NY 10001|(212) 594-8939|4.0 stars|open'}
```


##### 2) url(testing or prod)/upgrade 

Upgrades a user to a certain account type 

**Examples:** 
```
//To add 40 text messages
Arguments - {Texts: 40, From: 5734894023, Key: "bT7KZhQZUQ"}
Response - {success:True} 
```

##### 3) url(testing or prod)/signup 

Upgrades a user to a certain account type 

**Examples:** 
```
//To add allow user signup
Arguments - {Email: amni2015@gmail.com, From: 5734894023, Key: "bT7KZhQZUQ"}
Response - {success:True} 
```

### Version 0.2
*last updated 2/1/15*


