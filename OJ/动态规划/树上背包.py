m, n = map(int, input().split())
adjacency = [[] for _ in range(n+1)]
price, value = [0], [0]
in_degree = [0 for _ in range(n+1)]

for _ in range(1,n+1):
    temp = list(map(int, input().split()))
    price.append(temp[0])
    value.append(temp[1])
    if temp[2]:
        adjacency[temp[2]].append(_)
        in_degree[_] += 1

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

def dfs(u):
    sons = adjacency[u]
    if sons != []:
        for i in range(0, len(sons)): # 遍历子节点物品
            dfs(sons[i])
            for j in range(m-price[u], price[sons[i]]-1,-1): # 遍历分配给子节点的容量
                for k in range(0,j+1):
                    dp[u][j] = max(dp[u][j], dp[u][j-k] + dp[sons[i]][k])
    for j in range(m,price[u]-1,-1):
        dp[u][j] = dp[u][j-price[u]] + price[u]*value[u]

beg = []
for u in range(1,n+1):
    if in_degree[u] == 0:
        beg.append(u)

if len(beg) == 1: # 连通图
    dfs(beg[0])
    print(dp[beg[0]][m])
else: # 不连通图
    for u in beg:
        adjacency[0].append(u)
        in_degree[u] += 1
    dfs(0)
    print(dp[0][m])
    

