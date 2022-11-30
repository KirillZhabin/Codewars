# https://www.codewars.com/kata/62e66bea9db63bab88f4098c

from itertools import *
from math import *

def find_them(n,p):
    f = lambda x: x*(x+1)//2
    s = 0
    for i in range(1,len(p)+1):
        for c in combinations(p,i):
            x = prod(c)
            s += (-1)**(i+1)*x*f((n-1)//x)
    return s