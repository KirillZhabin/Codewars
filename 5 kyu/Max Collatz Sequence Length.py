# https://www.codewars.com/kata/53a9ee602f150d5d6b000307

def max_collatz_length(n):
    if type(n) != int or n < 1:
        return []
    seq, max_len, max_num = [0] * n, 0, 0
    for x in range(1, n + 1):
        if seq[x - 1]:
            continue
        i, l = x, 1
        while x > 1:
            if x % 2:
                x = x // 2 * 3 + 2
                l += 2
            else:
                x //= 2
                l += 1
            if x <= n and seq[x - 1]:
                l += seq[x - 1] - 1
                break
        seq[i - 1] = l
        if l > max_len:
            max_len, max_num = l, i
    return [max_num, max_len]