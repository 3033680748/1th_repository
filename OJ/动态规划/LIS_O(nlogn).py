li = list(map(int, input().split())) # ��֤��������
n = len(li)
dp = [0] # dp[0]ι��,dp[i]��ʾ����Ϊi���Ӵ��Ľ�β����С��Ԫ��
# dp����֤���ǲ��ݼ���

from bisect import bisect_left

for i in range(n):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        x = bisect_left(dp,li[i])
        dp[x] = li[i]

ans = len(dp) - 1
print(ans)