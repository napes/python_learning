
s = '2*x +3'
x = 4
result = eval(s)
print(result)

import re
s = '2x + 3 + 3xxx +29x + 30x - 12x^2'
s = s.replace(' ','')
# p = re.compile('\w+')
p = re.compile('[+-]?\w+')
p.findall(s)


s = '2x**2'
i = s.find('x')
if i > 0:
    s = s[:i]+'*'+s[i:]
else:
    s = s
print(s)

# s = s[:i]
# print(s)
# s = s[:i]+s[i:]
# print(s)

q = '2x'
q = q[1:]
print(q)

# for t in terms:
#     i = t.find('x')
#     if i > 0:
#         t = t[:i]+'*'+t[i:]
#     else:
#         t = t
#     print(t)

################################


## strip spaces, swap ^ for **
s1 = '2x +3'
s2 = '2x + 3 + 3x +29x + 30x - 12x^22'
s3 = '1 +2x+3x^2'
s = s1
s = s.replace(' ','')
s = s.replace('^','**')



## 

## regular expression to parse out the variables
import re

# p = re.compile('[+-]?\w+') ## this doesnt bring in ^2
# p = re.compile('[+-]?[\w]+[\w^\w]?') ## this doesnt work because need to make ^ valid as part of exrpression
# p = re.compile('[+-]?[\w^]+') ## valid! but make one for "**"

p = re.compile('[+-]?[\w*]+')
terms = p.findall(s)
print(terms)

## need to insert * between digit and x

for i, t in enumerate(terms):
    pos = t.find('x')
    if pos > 0:
        terms[i] = t[:pos]+'*'+t[pos:]
    else:
        terms[i] = t
    print(t)

## join all the terms, prepare for eval
formula = ''.join(terms)

x = 3
result = eval(formula)
print(x,formula,result,sep='\n')

# print(x,formula,sep='\n')

