s = 'Pig latin is cool' # igPay atinlay siay oolcay
s2 = 'Hello world !' # elloHay orldway !

import re

def pig_it(text):

    match = re.findall(r'\w+',text)

    punct = re.findall(r'[?.!]',text) ##hackish... asusumes final placement

    l = []
    
    for i,x in enumerate(match):
        w = match[i]
        w = w[1:] + w[0] + 'ay'
        l.append(w)
    l = l + punct    
    l = ' '.join(l)
    return l

string = s2
pig_it(string)