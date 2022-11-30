# https://www.codewars.com/kata/5977ef1f945d45158d00011f

from itertools import zip_longest

def sep_str(st): 
    return list(map(list, zip_longest(*st.split(), fillvalue='')))