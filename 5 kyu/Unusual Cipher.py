# https://www.codewars.com/kata/5efdde81543b3b00153e918a

import re

def encipher(s, key):
    s, key = s.lower(), key.lower()
    flag = False
    if "j" in key:
        if "i" not in key or key.index("j") < key.index("i"):
            flag = True
    s_org = s
    lst = []
    cnt = 0
    for c in key.replace("j","i").replace(" ",""):
        if c not in lst:
            lst.append(c)
    for c in "abcdefghiklmnopqrstuvwxyz":
        if c not in lst:
            lst.append(c)    
    
    s = s.replace("j","i").replace(" ","")
    while re.search(r"(.)\1", s):
        s = re.sub(r"(.)\1", r"\1x\1", s)
    
    res = ""
    for c1, c2 in zip(s[::2], s[1::2]+"x"):
        v1, v2 = lst.index(c1), lst.index(c2)
        if v1//5 == v2//5:
            res += lst[5*(v1//5)+(v1+1)%5] + lst[5*(v2//5)+(v2+1)%5]
        elif v1%5 == v2%5:
            res += lst[(v1+5)%25] + lst[(v2+5)%25]
        else:
            res += lst[5*(v1//5)+v2%5] + lst[5*(v2//5)+v1%5]
    res = res.upper()
    
    if flag: res = res.replace("I", "J")
    
    out = ""
    cnt=0
    for x in s_org:
        if x == " ": out += x
        else:
            out += res[cnt]
            cnt += 1
    return out + res[cnt:]