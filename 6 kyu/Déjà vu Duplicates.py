# https://www.codewars.com/kata/547f601b4a437a2048000981

from collections import Counter as c
def find_duplicates(e):
    print(e)
    x = []
    y = []
    for i in e:
        if not i in x:
            x.append(i)
        else:
            y.append(i)
    e[:] = list(c(e))
    return y