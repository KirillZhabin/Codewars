def merge_arrays(first, second): 
    arr=[]
    for i in second:
        if i not in arr:
            arr.append(i)
    for j in first:
        if j not in arr:
            arr.append(j)
    res_arr = sorted(arr)
    return res_arr