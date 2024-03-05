T, n = map(int, input().split())

weight, val = [], []

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    val.append(v)

#方法1：二维dp

dp = [[0 for _ in range(T+1)] for _ in range(n)]

for i in range(1,T+1):
    if i >= weight[0]:
        dp[0][i] = val[0]

for i in range(1,n):
    for j in range(1,T+1):
        if j < weight[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+val[i])

print(dp[n-1][T])

#方法2：滚动数组,先物品后重量，重量倒叙遍历
#实际上是重复利用，循环覆盖，以达到了压缩状态的目的
dp = [0 for _ in range(T+1)]

for i in range(n):
    for j in range(T,0,-1):
        if j < weight[i]:
            dp[j] = dp[j]
        else:
            dp[j] = max(dp[j],dp[j-weight[i]]+val[i])


print(dp[T])