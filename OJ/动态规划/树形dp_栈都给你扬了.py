n = int(input())

happy = [-1]

in_degree = [0 for _ in range(n+1)]
adjacency = [[] for _ in range(n+1)]

for _ in range(n):
    happy.append(int(input()))

big_boss = []
low_class = []
for _ in range(n-1):
    temp = list(map(int, input().split()))
    adjacency[temp[1]].append(temp[0])
    in_degree[temp[0]] += 1

for _ in range(1,n+1):
    if in_degree[_] == 0:
        big_boss.append(_)
    if adjacency[_] == []:
        low_class.append(_)

global dp
dp = [[0,0] for _ in range(n+1)]

def dfs(i):
    if adjacency[i] == []:
        dp[i][1] = happy[i]
    else:
        for low in adjacency[i]:
            dfs(low)
        for low in adjacency[i]:
            dp[i][1] += dp[low][0]
        dp[i][1] += happy[i]
        for low in adjacency[i]:
            dp[i][0] += max(dp[low][0],dp[low][1])

ans = 0
for i in big_boss:
    dfs(i)
    ans += max(dp[i][0],dp[i][1])

print(ans)
