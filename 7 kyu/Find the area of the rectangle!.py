import math
def area(d, l): 
    if d == l or d < l:
        return "Not a rectangle"
    s = math.sqrt(d ** 2 - l ** 2)
    return round(l * s, 2)