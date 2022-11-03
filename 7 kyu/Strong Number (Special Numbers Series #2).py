def strong_num(number):
    sum = 0
    temp = number
    while number:
        i = 1
        f = 1
        r = number % 10
        while(i <= r):
            f = f * i
            i = i + 1
        sum += f
        number //= 10
    
    if sum == temp:
        return("STRONG!!!!")
    else:
        return("Not Strong !!")