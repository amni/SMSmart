import wikipedia 


def summary(term, sentences = 5):
    """Summarizes first x sentences of a specific topic"""
    try: 
        summary = wikipedia.summary(term, sentences)
        searched_term = wikipedia.search(term)[0]
        result = '||'.join([searched_term, summary])
    except wikipedia.exceptions.DisambiguationError as DisambiguationError:
        result = '1'
    except wikipedia.exceptions.PageError as PageError: 
        result = '2'
    except: 
        result = '3'
    return result

def search(term, limit = 3):
    """Perform search of a specific term producing multiple results"""
    try:
        search_results = wikipedia.search(term, limit)
        result = '^^'.join(search_results)
    except wikipedia.exceptions.DisambiguationError as DisambiguationError:
        result = '1'
    except wikipedia.exceptions.PageError as PageError: 
        result = '2'
    except: 
        result = '3'        
    return result
