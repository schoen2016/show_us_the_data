import re

def pre_process(text):
    
    # text to lower case
    text = text.lower()

    # remove tags
    text = re.sub("&lt;/?.*?&gt;"" &lt;&gt; ", text)

    # remove special char and digits
    text = re.sub("(\\d|\\W)+"," ",text)

    return text