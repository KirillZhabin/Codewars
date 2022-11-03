def array_plus_array(arr1,arr2):
    sum_arr1 = 0
    sum_arr2 = 0
    
    for i in range(len(arr1)):
        sum_arr1 += int(arr1[i])
        
    for j in range(len(arr2)):
        sum_arr2 += int(arr2[j])
    
    res = sum_arr1 + sum_arr2
    
    return res