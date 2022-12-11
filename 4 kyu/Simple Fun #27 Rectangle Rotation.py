# https://www.codewars.com/kata/5886e082a836a691340000c3

def rectangle_rotation(a, b):
    a //= 2**0.5
    b //= 2**0.5
    r = (a + 1) * (b + 1) + a * b

    return r + r % 2 - 1