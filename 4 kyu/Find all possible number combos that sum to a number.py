# https://www.codewars.com/kata/555b1890a75b930e63000023

def combos(n, m = 1):
    if n < m:
        return []
    res = [[n]]
    for i in range(m, n):
        l = [i]
        for j in combos(n - i, i):
           res += [l + j]
    return res