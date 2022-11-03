def name_shuffler(str):
    new_str = str.split()
    new_str.reverse() 
    res_str = " ".join(new_str)
    return res_str