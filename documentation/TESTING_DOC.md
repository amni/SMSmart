# SMSmart Testing Documentation

Tests are located throughout the codebase:
- for tests on queries: ```backend/tests.py```
- for tests on the parser: ```backend/parser/test.py```
- for tests on the subprograms: ```backend/controller/api/tests/```
- for tests on the subprogram wrappers: ```backend/controller/api/verbose_tests```

To run all the tests, simply execute the harness script in backend/ dir:  ```./backend/test_harness.sh```

**Instructions**:
- to run all the tests in one module: ```python tests.py```
- to run tests from one class: ```python tests.py TestMain```
- to run specific tests from one class: ```python tests.py TestWikipedia.test_wiki_summary```


##### TestDistribute 
Methods:
- **test_distribute** - currently turned off, used to check whether distributed texting works

##### TestOnboard
Methods:
- **test_onboard** 

##### TestWikipedia
Methods:
- **test_wiki_search**
- **test_wiki_limit** - tests with invalid limits (negative numbers) and large limits (>1000)
- **test_wiki_summary**
- **test_wiki_summary_error** - tests Wikipedia with disambiguation error and invalid term (no page found) error

##### TestYelp
Methods:
- **test_yelp** - tests yelp with location string 
- **test_yelp_geo** - tests yelp with lat/lng coordinates 
- **test_yelp_error** - first tests with invalid category, then with invalid location

##### TestMaps
Methods:
- **test_maps** - test maps with from location as location string
- **test_maps_geo** - test maps with from location as lat/lng coordinate
- **test_maps_missing_space** - test specific maps query where return value is missing space before the word ```Destination```
- **test_maps_error** - test maps with invalid from/to locations 

##### TestUnicode
Methods:
- **test_unicode** - test queries that return non ASCII unicode 

##### TestMain
Methods:
- **test_main** - stress test that runs through queries for all programs

### Version 0.1 
*last updated 12/28/14*


