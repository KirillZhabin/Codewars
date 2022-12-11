# https://www.codewars.com/kata/5e417587e35dfb0036bd5d02

def path_counter(con):
    
    out = [[-1]*len(con[0]) for i in range(len(con))]
    f = 0,0
    for y in range(len(con)):
        for x in range(len(con[0])):
            if con[y][x] == 'f':
                f = y,x
                break
    out[f[0]][f[1]] = 0
    dirs = {(0,1):'l', (0,-1):'r', (1,0):'u', (-1,0):'d'}
    stack = [f]
    while stack:
        y,x = stack.pop()
        for dy, dx in dirs.keys():
            ny, nx = (y+dy) % len(con), (x+dx) % len(con[0])
            if con[ny][nx] == dirs[(dy,dx)]:
                out[ny][nx] = out[y][x] + 1
                stack.append((ny,nx))
    return out