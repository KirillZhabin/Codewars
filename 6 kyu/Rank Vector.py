# https://www.codewars.com/kata/545f05676b42a0a195000d95

def ranks(a):
    b = sorted(a)[::-1]
    return [b.index(j)+1 for j in a]