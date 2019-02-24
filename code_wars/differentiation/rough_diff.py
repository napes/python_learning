

t = '+2*x**2'

import re

t = ['+2*x**2', '+3', '2*x', '15']



def diff(term):
    exp = 0
    new_exp = 0
    c = 0 
    # print(term)
    # p = re.compile('([+-]?)([\w])([\D]?)')
    # p = re.compile('([+-]?)(\w)([0-9]+)?') #doesnt quite work
    p = re.compile('([+-]?)([\d]*).*?([\d]*)$')
        #.*? matches whole string
        # then any digits
        # $ matches to end of string
    
    m = p.match(term)
    print(m.groups())
    print(m.group(1),m.group(2),m.group(3))

## re groups:
    #1 sign (none, +, -)
    #2 number (none, 1 digit, multiple)
    #3 exponent ()

    
    exp = m.group(3)
    print('exp: ',exp)

    if exp == '':
        new_exp = 0
        exp = 1
    else:
        new_exp = int(m.group(3))-1
    print('exp: ',exp)
    print('new_exp: ', new_exp)
    
    sign = m.group(1)
    print('sign: ', sign)
    print('group: ', m.group(2))
    c = int(m.group(2)) * int(exp)
    print('c: ', c)    
    # new_exp = str(new_exp)

    # print(sign, 'c: ', c, new_exp)
    # result = sign + c + 'x**' + new_exp
    # print(result)
    test = c * 10
    if c == 0:
        term = 0
    elif new_exp == 0 and exp == 0:
        term = 0
    else:
        term = str(c) + 'x**' + str(new_exp)
    print(term)

diff(t[1])