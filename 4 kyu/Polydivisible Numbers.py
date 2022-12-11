# https://www.codewars.com/kata/556206664efbe6376700005c

CHARS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def is_polydivisible(s, b):
    total=0
    for x,d in enumerate(s):
        total=b*total+CHARS.index(d)
        if total%(x+1):
            return False
    return True
        

def get_polydivisible(n, b):
    digits=lambda x:digits(x//b)+CHARS[x%b] if x else ''
    count,x=1,0
    while count<n:
        x+=1
        if is_polydivisible(digits(x),b):
            count+=1
    return digits(x) if x else '0'