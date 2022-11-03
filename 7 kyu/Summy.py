def summy(string_of_ints):
    
    arr = string_of_ints.split()
    sum = 0
    
    for i in arr: 
        sum += int(i)
    return sum