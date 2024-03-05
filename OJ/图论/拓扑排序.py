n, m = map(int, input().split())

in_degree = [0 for _ in range(n+1)]

adjacency = [[0]] + [[] for _ in range(n)]

for i in range(m):
    temp = list(map(int, input().split()))
    adjacency[temp[0]].append(temp[1])
    in_degree[temp[1]] += 1

# 
beg = []
for i in range(1,n+1):
    if in_degree[i] == 0:
        beg.append(i)
#
end = []
for i in range(1,n+1):
    if adjacency[i] == []:
        end.append(i)

from collections import deque

dp = [0 for _ in range(n+1)]
queue = deque([])

for idx in beg:
    queue.append(idx)
    dp[idx] = 1

while len(queue):
    curNode = queue[0]
    queue.popleft()
    for nextNode in adjacency[curNode]:
        in_degree[nextNode] -= 1
        dp[nextNode] += dp[curNode]
        if in_degree[nextNode] == 0:
            queue.append(nextNode)
    
ans = 0
for idx in end:
    ans += dp[idx]

print(ans%80112002)
