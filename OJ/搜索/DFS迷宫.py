N, M, T = list(map(int, input().split()))
maze = [[0 for _ in range(M)] for _ in range(N)]
SX, SY, FX, FY = map(int, input().split())

SX, SY, FX, FY = SX - 1, SY - 1, FX - 1, FY - 1

for i in range(T):
    x, y = map(lambda x: x - 1, map(int, input().split()))
    maze[x][y] = 1

vis = [[0 for _ in range(M)] for _ in range(N)]

ans = 0
dire = [
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
    lambda x,y:(x+1,y)
]

def search(i, j):
    if i == FX and j == FY:
        global ans
        ans += 1
    else:
        if -1 < i < N and -1 < j < M and vis[i][j] == 0 and maze[i][j] == 0:
            vis[i][j] = 1
            for k in range(4):
                search(dire[k](i, j)[0], dire[k](i, j)[1])
            vis[i][j] = 0


search(SX, SY)

print(ans)