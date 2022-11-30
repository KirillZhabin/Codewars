# https://www.codewars.com/kata/55a5d97d81a010881800004a

def lastvowel(ch):
    ab = 'abcdefghijklmnopqrstuvwxyz'
    if ch.lower() not in ab: 
	return ch
    if ch.lower() in 'aeiou': 
	return ch
    idx = ab.find(ch.lower())
    if idx > 20: 
	return ch + 'u'
    elif idx > 14: 
	return ch + 'o'
    elif idx > 8: 
	return ch + 'i'
    elif idx > 4: 
	return ch + 'e'
    elif idx > 0: 
	return ch + 'a'
    else: 
	return ch
    
def toexuto(text):
    return ''.join(map(lastvowel, text))