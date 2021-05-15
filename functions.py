# look for terms in tweet
def find_terms(terms, text):
    found = False
    for term in terms:
        if term in text:
            found = True
    return found
