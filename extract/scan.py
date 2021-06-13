
import util.nlp_helper as nlph
    
def isMatch(pattern, text, pos):
    for i in range(0,len(pattern)):
        cur = pos+i
        if cur < len(text) and pattern[i].lower() != text[cur].lower():
            return False

    return True


def isNoise(t, text, pattern)
    # True: first word in pattern is not found at text[t] to text[t+padding]

    end = t+padding if len(text) < t+padding else len(text)

    for i in range(t, end):
        if text[t].lower() == pattern[0].lower():
            return False

    return True 

def find_pattern(text, pattern, padding):
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


def find_noise(text, pattern, padding):
    noise_list = list()
    for t in range(0,len(text)):
        if isNoise(t, text, pattern):
            noise_list.append(text[t:t+padding])

    i = random.randint(0,len(letters)-1)
    found = [noise_list[i]]


def scan(pattern, text, options={}):

    # read options
    padding = options['padding'] if 'padding' in options.keys() else 3
    remove_stopwords = options['remove_stopwords'] if 'remove_stopwords' in options.keys() else False
    noise = option['noise'] if 'noise' in options else False

    h = nlph.NLPHelper(remove_stopwords=remove_stopwords)

    # tokenize and remove stopwords
    text = h.token_rsw(text)
    pattern = h.token_rsw(pattern)

    func = find_noise if noise else find_pattern

    return func(text, pattern, padding)
