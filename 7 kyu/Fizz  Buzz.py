def solution(number):
    a = 0
    b = 0
    c = 0
    for n in range(3, number):
        if n % 15 == 0:
            c += 1
        elif n % 5 == 0:
            b += 1
        elif n % 3 == 0:
            a += 1
    return [a, b, c]