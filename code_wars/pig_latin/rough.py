s = 'Pig latin is cool' # igPay atinlay siay oolcay
s2 = 'Hello world !' # elloHay orldway !

import re

# split = re.split(r'\s+', s2)
# print(split,type(split))

# w = split[0]
# w = w[1:] + w[0] + 'ay'
# print(w,type(w))

## issue with this approach is that it splits by whitespace...
## includes punctuation, better to do a findall of words

match = re.findall(r'\w+',s2)
print(match,type(match))

punct = re.findall(r'[?.!]',s2)
print(punct,type(punct))

# w = match[0]
# w = w[1:] + w[0] + 'ay'
# print(w,type(w))

# l = list()
l = []
for i,x in enumerate(match):
    w = match[i]
    w = w[1:] + w[0] + 'ay'
    print(w)
    l.append(w)
    print(l,'\n\n')
l = ' '.join(l)+ ' ' + punct[0]
print(l)