m, n = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

memo = [0 for _ in range(n+1)]

for j in range(1,n+1):
    dp[1][j] = 1
    memo[j] = (memo[j-1]+dp[1][j]) % 1e4

for i in range(2,m+1):
    if i % 2: # 奇数
        temp = [0 for _ in range(n+1)]
        for j in range(1,n+1):
            dp[i][j] = memo[j-1] % 1e4
            # 滚动数组更新前缀和数组
            temp[j] = (temp[j-1]+dp[i][j]) % 1e4
        memo = temp.copy()
    else: # 偶数
        for j in range(1,n+1):
            dp[i][j] = (memo[-1]-memo[j]) % 1e4
            # 同上
            memo[j] = (memo[j-1]+dp[i][j]) % 1e4

ans = 0
for _ in range(1,n+1):
    ans = (dp[m][_] + ans) % 1e4

print(int(ans))    
