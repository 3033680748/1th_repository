li = list(map(int, input().split()))
n = len(li)

# 第一问,求最长不上升子序列
ans1 = 0
dp = [9999999]
from collections import deque
from bisect import bisect_left
dp = deque(dp)
dp.appendleft(li[0])
for i in range(1,n):
    if li[i] <= dp[0]:
        dp.appendleft(li[i])
    else:
        # 二分查找,不递增数组,第一个不大于的
        x = bisect_left(dp, li[i])-1
        dp[x] = li[i]
ans1 = len(dp)-1
print(ans1)

# 第二问
ans2 = 0
system = [li[0]]
for i in range(1,n):
    if li[i] > system[-1]:
        system.append(li[i])
    else:
        x = bisect_left(system,li[i])
        system[x] = li[i]

ans2 = len(system)
print(ans2)