# https://www.codewars.com/kata/5fe919c062464e001856d70e

from math import degrees, acos
from bisect import bisect_right

def windmill(S):
    if len(S) <= 1:
        return 0

    rotations = {}
    for i in range(len(S)):
        res = []
        for j in range(len(S)):
            if i != j:
                dx, dy = S[j][0] - S[i][0], S[j][1] - S[i][1]
                deg = degrees(acos(dy / (1 * (dx ** 2 + dy ** 2) ** 0.5)))
                res.append((round(180 - deg if dx < 0 else deg, 4), j))
        res.sort()
        rotations[S[i]] = [[deg for deg, _ in res], [p for _, p in res]]

    cd, cp, half_turn = 0.0, (0, 0), 0
    for x in range(10**9):
        degs, points = rotations[cp]
        i = bisect_right(degs, cd)
        half_turn += i == len(degs)
        cd = degs[i % len(degs)]
        if cd >= 180.0:
            cd = 0
            half_turn += 1
        cp = S[points[i % len(degs)]]
        if half_turn >= 2:
            return x