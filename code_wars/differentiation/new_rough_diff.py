import re

t = ['+2*x**2', '+3', '2*x', '15']



def diff_one(term):
    
    exp = 0
    new_exp = 0
    c = 0 
    p = re.compile('([+-]?)([\d]*)([\D]*).*?([\d]*)$')
    m = p.match(term)
    print(m.groups())
    
    d = dict()
    d['sign'] = m.group(1)
    d['c'] = m.group(2)
    d['x'] = m.group(3)
    d['exp'] = m.group(4)

    if d['c'] == '':
        c = 0
    else:
        c = int(d['c'])
    if d['exp'] == '':
        exp = 0
    else:
        exp = int(d['exp'])
    new_exp = exp - 1

    if d['x'] == '':
        term = 0
    else:
        term = str(c * exp) + '*x**' + str(new_exp)



    print(c,exp,new_exp)
    print(d)
    print('term: ', term)
    # print(c,exp,new_exp)

diff_one(t[2])

def diff(terms):
    # for t in terms:
    #     ##########
    exp = 0
    new_exp = 0
    c = 0 
    p = re.compile('([+-]?)([\d]*)([\D]*).*?([\d]*)$')
    m = p.match(t)
    print(m.groups())
    
    d = dict()
    d['sign'] = m.group(1)
    d['c'] = m.group(2)
    d['x'] = m.group(3)
    d['exp'] = m.group(4)

    if d['c'] == '':
        c = 0
    else:
        c = int(d['c'])
    if d['exp'] == '':
        exp = 0
    else:
        exp = int(d['exp'])
    new_exp = exp - 1

    if d['x'] == '':
        term = 0
    else:
        term = str(c * exp) + '*x**' + str(new_exp)



    print(c,exp,new_exp)
    print(d)
    print('term: ', term)
    # print(c,exp,new_exp)

diff_one(t[2])
