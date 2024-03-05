maze = []
for _ in range(30):
    maze.append(input())

vis = [[0 for _ in range(60)] for _ in range(30)]

from collections import deque

ans = 0

dire = [
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
    lambda x,y:(x+1,y)
    ]

for i in range(30):
    for j in range(60):
        queue = deque([])
        if maze[i][j] == '1' and vis[i][j] == 0:
            queue.append([i,j])
            vis[i][j] = 1
            temp = 0
            while len(queue):
                cur_ = queue[0]
                for k in range(4):
                    x, y = dire[k](cur_[0],cur_[1])
                    if -1<x<30 and -1<y<60 and maze[x][y] == '1' and vis[x][y] == 0:
                        queue.append([x,y])
                        vis[x][y] = 1 # 当加入队列时就要设置为已经访问
                temp += 1
                queue.popleft()
            else:
                ans = max(ans, temp)

print(ans)
