s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
n1 = len(s1)
n2 = len(s2)
# O(n^2)

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1,n1+1):
    for j in range(1,n2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ans = dp[n1][n2]

# O(nlogn)
'''
����Ϊʲô����ת����LIS���⣬�����ṩһ�����͡�

A:3 2 1 4 5

B:1 2 3 4 5

���ǲ������������±���ţ���3���a,��2���b����1���c�������Ǳ�ɣ�

A: a b c d e
B: c b a d e

�������֮��LCS������Ȼ����ı䡣���ǳ�����һ�����ʣ�

�������е������У�һ����A�������С���A������ǵ��������ġ�
�������������ǵ��������ġ�

���仰˵��ֻҪ�����������B�е���������������A�������С�

�ĸ���أ���Ȼ��B��LIS���

�Դ����ת����
'''
