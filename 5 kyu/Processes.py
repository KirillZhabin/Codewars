# https://www.codewars.com/kata/542ea700734f7daff80007fc

def processes(start, end, p):
    q = [[[],start,p]]
    res = []
    while q:
        r,s,pro = q.pop(0)
        for t,a,b in pro:
            if a == s:
                x = pro[:]
                x.remove([t,a,b])
                q.append([r+[t],b,x])
                if b == end:
                    res.append(r+[t])
    return [] if not res else res[0]