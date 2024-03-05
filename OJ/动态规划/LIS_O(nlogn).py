li = list(map(int, input().split())) # 保证都是正数
n = len(li)
dp = [0] # dp[0]喂狗,dp[i]表示长度为i的子串的结尾的最小的元素
# dp可以证明是不递减的

from bisect import bisect_left

for i in range(n):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        x = bisect_left(dp,li[i])
        dp[x] = li[i]

ans = len(dp) - 1
print(ans)