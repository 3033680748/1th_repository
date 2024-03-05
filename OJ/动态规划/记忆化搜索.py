r, c = map(int, input().split())

maze = []

for i in range(r):
    maze.append(list(map(int, input().split())))

ans = [[0 for _ in range(c)] for _ in range(r)]

dire = [
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
    lambda x,y:(x+1,y)
    ]

# 记忆化搜索

def search(i,j):
    if ans[i][j] != 0:
        return ans[i][j]
    else:
        ans[i][j] += 1
        temp = 0
        for k in range(4):
            x, y = dire[k](i,j)
            if -1<x<r and -1<y<c and maze[x][y]>maze[i][j]:
                temp = max(search(x,y), temp)
        ans[i][j] += temp
        return ans[i][j]

out_ = 0

for i in range(r):
    for j in range(c):
        search(i,j)
        out_ = max(out_, ans[i][j])

print(out_)
