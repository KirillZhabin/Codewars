# https://www.codewars.com/kata/56c0ca8c6d88fdb61b000f06

def next_version(version):
    
    def rec_h(arr):
        if len(arr) == 1:
            return [str(int(arr[0]) + 1)]
        else:
            tmp = int(arr[-1]) + 1
            if tmp == 10:
                return rec_h(arr[:-1]) + ['0']
            else:
                return arr[:-1] + [str(tmp)]
    
    res = rec_h(version.split('.'))
    
    return '.'.join(res)