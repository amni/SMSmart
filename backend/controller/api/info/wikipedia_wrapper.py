import wikipedia 


def summary(term):
    try:
        result = wikipedia.summary(term)
    except:
        result = "Disambiguation Error: Try searching for exactly what you want"
    return result

def search(term, limit = 3):
    ret_list = wikipedia.search(term, limit)
    return ret_list


results = search("John")
print results

for r in results:
    print summary(r)


