
T, n = map(int, input().split())

weight, val, amount = [], [], []

for _ in range(n):
    w, v, a = map(int, input().split())
    weight.append(w)
    val.append(v)
    amount.append(a)

# 多重背包的朴素方法

dp = [0 for _ in range(T+1)]

for i in range(n):
    for j in range(T,0,-1): # 注意倒序
        for k in range(amount[i]+1):
            if k*weight[i] > j:
                break
            else:
                dp[j] = max(dp[j], dp[j-k*weight[i]]+k*val[i])




