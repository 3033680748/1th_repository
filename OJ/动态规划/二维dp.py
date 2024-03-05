n = int(input())
li = list(map(int, input().split()))

# dp = [[1 for _ in range(40001)] if _ == 0 else [0 for _ in range(40001)] for _ in range(n)] # 公差为0到200000，0到-200000(20001,400001)
dp = [[0 for _ in range(40001)] for _ in range(n)]

# 998244353
ans = 0
for i in range(0,n):
    ans += 1
    for j in range(i-1,-1,-1):
        d = li[i] - li[j]
        dp[i][d] += dp[j][d] + 1
        ans = (ans+dp[j][d]+1) % 998244353
        dp[i][d] = dp[i][d] % 998244353

print(ans)