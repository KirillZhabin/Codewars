def solve(s):
    res1 = 0
    res2 = 0

    for i in s:
        if i in 'aeiouAEIOU':
            res2 += 1
            if res2 > res1:
                res1 = res2
        else:
            res2 = 0
    return res1