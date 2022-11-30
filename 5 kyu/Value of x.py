# https://www.codewars.com/kata/614ac445f13ead000f91b4d0

def solve(eq):
    a,b = eq.replace('x','0').split('=')
    x = eval(a) - eval(b)
    if '- x' in eq: x*=-1
    return x if eq.index('x') > eq.index('=') else -x