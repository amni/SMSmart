import wikipedia 


def summary(term, sentences = 3):
    try:
        summary = wikipedia.summary(term, sentences)
        searched_term = wikipedia.search(term)[0]
        result = searched_term + '^' + summary
    except:
        result = "Disambiguation Error: Try searching for exactly what you want"
    return result

def search(term, limit = 3):
    ret_list = wikipedia.search(term, limit)
    return ret_list





