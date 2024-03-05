n = int(input())

tree = [[0 for _ in range(n)] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for idx,num in enumerate(temp):
        tree[i][idx] = num

dp[0][0] = tree[0][0]

for i in range(1,n):
    for j in range(i+1):
        try:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tree[i][j]
        except:
            dp[i][j] = dp[i-1][j-1] + tree[i][j]

out = -1
for k in range(n):
    out = max(out, dp[n-1][k])

print(out)