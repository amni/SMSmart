import wikipedia 


def summary(term, sentences = 3):
    """Summarizes first x sentences of a specific topic"""
    summary = wikipedia.summary(term, sentences)
    searched_term = wikipedia.search(term)[0]
    result = '^'.join([searched_term, summary])
    return result

def search(term, limit = 3):
    """Perform search of a specific term producing multiple results"""
    search_results = wikipedia.search(term, limit)
    result = '^'.join(search_results)
    return result
