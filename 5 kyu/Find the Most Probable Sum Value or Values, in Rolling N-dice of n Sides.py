# https://www.codewars.com/kata/56fb9da2fca8b9d7de00083f

from itertools import product

def most_prob_sum(dice, n):
    d_dct = {'tetrahedral':[1, 4], 
    'cubic':[1, 6], 
    'octahedral':[1, 8],
    'ninesides':[1, 9],
    'tensides':[1, 10],
    'dodecahedral':[1, 12],
    'icosahedral':[1, 20]}

    cube = d_dct[dice]

    d_val = []
    for i in range(1, cube[1]+1):
        d_val.append(i)
    perm = list(product(d_val, repeat = n))

    dct = {}
    for lst in perm:
        sum_ = sum(lst)
        if sum_ not in dct:
            dct[sum_] = 0
        dct[sum_] += 1

    for k, v in sorted(dct.items()):
        dct[k] = v/(len(perm))   
    
    prob = max(dct.values())
    nums = []
    for num, val in sorted(dct.items()):
        if val == prob:
            nums.append(num)
    return [nums, prob]