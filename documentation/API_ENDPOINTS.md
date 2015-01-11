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
//Possible Plans PLANS = ["Budget":50, "Pro": 100, "Premium":200, "Unlimited": 10000]
Arguments - {Account: "Budget", From: 5734894023}
Response - {success:True} 
```

### Version 0.1
*last updated 1/1/15*


