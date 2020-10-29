import re

def smart_split(text:str):
    '''
    Get rid of double spaces and punctiation in a STRING,
    make it lowercase and split it into a LIST
    '''
    PUNCTUATION = ['.', ',', ';', '\n', '!', '?']
    for symbol in PUNCTUATION:
        text = text.replace(symbol, ' ')
        
    text = re.sub(' +', ' ', text.lower())
    return text.split()

