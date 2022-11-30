# https://www.codewars.com/kata/58a664bb586e986c940001d5

def missing_alphabets(s):
    alf = "abcdefghijklmnopqrstuvwxyz"
    q = []
    for x in alf:
        q.append(s.count(x))
    sets = max(q)
    fin = []
    for x in alf:
        if s.count(x) != sets:
            fin.append(x*(sets-s.count(x)))
    return(''.join(fin))