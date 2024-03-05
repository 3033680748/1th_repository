n = int(input())

nums = list(map(int,input().split()))

k = int(input())

l = 2*k

ans = []

from collections import deque
from bisect import bisect_left, bisect_right

window = deque([])

# 初始化

up = min(n,l+1)

for j in range(0,up):
    if len(window) == 0:
        window.append(nums[j])
    else:
        if window[-1] <= nums[j]:
            window.append(nums[j])
        else:
            while len(window) and window[-1] > nums[j]:
                window.pop()
            else:
                window.append(nums[j])
ans.append(window[0])

for i in range(1,n):
    if nums[i-1] == window[0]:
        window.popleft()
    if (l+i+1) <= n-1:
        if window[-1] <= nums[l+i+1]:
            window.append(nums[l+i+1])
        else:
            while window[-1] > nums[l+i+1]:
                window.pop()
            else:
                window.append(nums[l+i+1])
    ans.append(window[0])

for _ in range(n):
    print(ans[_],sep=' ')
