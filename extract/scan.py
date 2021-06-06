
import util.nlp_helper as nlph
    
def isMatch(pattern, text, pos):
    for i in range(0,len(pattern)):
        cur = pos+i
        if cur < len(text) and pattern[i].lower() != text[cur].lower():
            return False

    return True

def scan(pattern, text, options={}):

    # read options
    padding = options['padding'] if 'padding' in options.keys() else 3
    remove_stopwords = options['remove_stopwords'] if 'remove_stopwords' in options.keys() else False
    
    h = nlph.NLPHelper(remove_stopwords=remove_stopwords)

    # tokenize and remove stopwords
    text = h.token_rsw(text)
    pattern = h.token_rsw(pattern)

    found = []
    # scan
    for t in range(0,len(text)):
        if text[t].lower() == pattern[0].lower() and isMatch(pattern, text, t):
            
            start = t-padding
            end = t+padding+len(pattern)

            # pattern and padding is less than text length
            if t <= len(pattern) and t+len(pattern)+padding <= len(text): 
                found.append(" ".join(text))
            
            # pattern found in front of text
            elif t <= len(pattern) and t+len(pattern)+padding < len(text): 
                found.append(" ".join(text[0:end]))

            # pattern found in middle of text
            elif t > len(pattern) and t+len(pattern)+padding <= len(text):
                found.append(" ".join(text[start:end]))
            
            # pattern found at end of text
            elif t > len(pattern) and t+len(pattern)+padding > len(text):
                found.append(" ".join(text[start:len(text)]))

            # Unaccounted for situation
            else: 
                found.append("Error: pattern not found")

    return found


