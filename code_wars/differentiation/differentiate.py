s1 = '2x +3'
s2 = '2x + 3 + 3x +29x + 30x - 12x^22'
s3 = '1 +2x+3x^2'
s = s1






import re


def get_terms(s):

    ## strip spaces, swap ^ for **
    s = s.replace(' ','')
    s = s.replace('^','**')

    ## regular expression to parse out the variables

    p = re.compile('[+-]?[\w*]+')
    terms = p.findall(s)

    ## need to insert * between digit and x
    ## TODO: make this better, use re and make it work for other vars besides x
    for i, t in enumerate(terms):
        pos = t.find('x')
        if pos > 0:
            terms[i] = t[:pos]+'*'+t[pos:]
        else:
            terms[i] = t
    
    # return terms and formula
    # formula = ''.join(terms)
    # d = dict()
    # d['terms'] = terms
    # d['formula'] = formula
    return terms
get_terms('2x^2 + 3')






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




def evaluate(s,x):
    
    terms = get_terms(s)

    ## join all the terms, evaluate
    formula = ''.join(terms)
    result = eval(formula)
    print(x,formula,result,sep='\n')
    return result

evaluate('2x^2 + 3', 2)
