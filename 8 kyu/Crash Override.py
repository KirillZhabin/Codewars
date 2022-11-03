def alias_gen(f_name, l_name):
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    
    f_name_first = f_name[0]
    l_name_first = l_name[0]
    
    if (not f_name_first.isalpha() or not l_name_first.isalpha()):
        return "Your name must start with a letter from A - Z."
    else:
        return FIRST_NAME[f_name_first] + " " + SURNAME[l_name_first]