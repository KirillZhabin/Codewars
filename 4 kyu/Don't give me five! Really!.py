# https://www.codewars.com/kata/621f89cc94d4e3001bb99ef4

import re

def dont_give_me_five(start, end):
    count = lambda n: int(re.sub(r'5(\d*)', lambda m: '4' + '9' * len(m[1]), str(n)).translate(str.maketrans("56789", "45678")), 9)
    if start > 0:
        return count(end) - count(start - 1)
    elif end < 0:
        return count(-start) - count(-end - 1)
    else:
        return count(end) + count(-start) + 1