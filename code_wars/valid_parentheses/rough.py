s1 = "()" #              =>  true
s2 = ")(()))" #         =>  false
s3 = "(" #               =>  false
s4 = "(())((()())())" # =>  true


# s = 'tthingaaa'

# s = s4

# l = {x: s.count(x) for x in s}
# print(l)

## if close is ever > open, break; if at end, open > close, break

# open = 0
# close = 0

s = s4

def func(string):
    open = 0
    close = 0

    for x in s:
        if close > open:
            return False
        elif x == '(':
            open += 1
        elif x == ')':
            close += 1
        elif close > open:
            return False
        print(open, close)

    if open > close:
        return False
    else:
        return True

func(s)
# if open > close:
#         return False
#         else:
#         return True