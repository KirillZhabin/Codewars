from math import *
def squares(x, n):
    a = [x]
    b = x
    if n < 1:
        return []
    for i in range(n - 1):
        a.append(b ** 2)
        b = b ** 2
    return a