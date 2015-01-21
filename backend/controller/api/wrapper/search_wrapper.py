# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
  
def perform_search(query, search_type = 'Web'):
    try: 
        #search_type: Web, Image, News, Video
        key= 'jHCJ4MWDJWHDt79H/hSp82vUFaMkyfrU/rdLAprylJA'
        query = urllib.quote(query)
        # create credential for authentication
        user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
        credentials = (':%s' % key).encode('base64')[:-1]
        auth = 'Basic %s' % credentials
        url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
        request = urllib2.Request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib2.build_opener()
        response = request_opener.open(request) 
        response_data = response.read()
        json_result = json.loads(response_data)
        result_list = json_result['d']['results']
        results = parse_results(result_list)
    except:
        results = "1"
    return results

def parse_results(results):
    parsed_results = []
    for result in results: 
        title = result["Title"]
        description = result["Description"]
        parsed_results.append(get_result([title, description]))
    return parsed_results

def get_result(variables):
    return "||".join(variables)

if __name__ == "__main__":
    main()