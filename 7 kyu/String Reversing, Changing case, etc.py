def reverse_and_mirror(s1, s2):
    sep_ = '@@@'
    s21 = s2[::-1].swapcase()
    s11 = s1[::-1].swapcase() + s1.swapcase()
    return s21 + sep_ + s11