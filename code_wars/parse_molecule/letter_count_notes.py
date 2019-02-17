string = 'tthingaaa'
ls1 = sorted(list(string))
#ls1 = sorted(ls1)
#ls = dict(string)
#print(ls)

ls2 = {x: ls1.count(x) for x in ls1}
print(ls2)

## none of this solves the bracketing / parentheticals

## regex will be needed to do this well...
## lower case next to uppercase is a unit, can have parenthetical inside bracket

def letter_count(s):
    l = sorted(list(s))
    d = {x: l.count(x) for x in l}
    return d

letter_count('helllooqqqqqqq')