import wikipedia 


def summary(term, sentences = 3):
    try:
        result = wikipedia.summary(term, sentences)
    except:
        result = "Disambiguation Error: Try searching for exactly what you want"
    return result

def search(term, limit = 3):
    ret_list = wikipedia.search(term, limit)
    return ret_list





