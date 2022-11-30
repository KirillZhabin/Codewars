# https://www.codewars.com/kata/5917fbed9f4056205a00001e

from itertools import combinations

def bananas(s):
    res = []
    for c in combinations(range(len(s)), len(s)-6):
        x = list(s)
        for i in c:
            x[i] = '-'
        x = ''.join(x)
        if x.replace('-', '') == 'banana':
            res.append(x)
    return res