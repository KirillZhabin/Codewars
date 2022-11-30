# https://www.codewars.com/kata/579ef9607cb1f38113000100

def operation(a,b):
    cnt = 0
    while bin(a).count('1') > 1:
        a >>= 1
        cnt += 1
    if a > b:
        a, b = b, a
    while a != b:
        a <<= 1
        cnt += 1
    return cnt