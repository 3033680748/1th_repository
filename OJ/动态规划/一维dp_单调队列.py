# 洛谷p1725
n, l, r = map(int, input().split())

froze = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

from collections import deque

window = deque([])

up_ = 0 - r
low_ = 0 - l


for i in range(1,n+1):
    # 单调队列优化,不严格递减,查找窗口最大值
    up_ += 1  # 上下边界
    low_ += 1
    # 检查出队
    if 0 <= up_-1 < n+1:
        if dp[up_-1] == window[0]:
            window.popleft()
    # 检查入队
    if 0 <= low_ < n + 1:
        while len(window) and window[-1] < dp[low_]:
            window.pop()
        else:
            window.append(dp[low_])
    # 状态转移
    if len(window) and window[0] != -9999999:
        dp[i] = window[0] + froze[i]
    else:
        dp[i] = -9999999

ans = -99999999999
for i in range(n-r+1, n+1):
    ans = max(ans, dp[i])

print(ans)