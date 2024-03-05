# 二进制优化，将每个物品按照2的次方数合成

T, n = map(int, input().split())

weight, val = [], []

for i in range(n):
    w, v, a = map(int, input().split())
    s = 1
    while s <= a:
        weight.append(s*w)
        val.append(v*s)
        a -= s
        s *= 2
    if a:
        weight.append(a*w)
        val.append(a*s)
n = len(weight)

dp = [0 for _ in range(T+1)]

for i in range(n):
    for j in range(T,0,-1):
        dp[j] = max(dp[j], dp[j-weight[i]]+val[i])

        