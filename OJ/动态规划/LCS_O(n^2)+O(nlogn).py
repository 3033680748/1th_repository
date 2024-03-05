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
关于为什么可以转化成LIS问题，这里提供一个解释。

A:3 2 1 4 5

B:1 2 3 4 5

我们不妨给它们重新标个号：把3标成a,把2标成b，把1标成c……于是变成：

A: a b c d e
B: c b a d e

这样标号之后，LCS长度显然不会改变。但是出现了一个性质：

两个序列的子序列，一定是A的子序列。而A本身就是单调递增的。
因此这个子序列是单调递增的。

换句话说，只要这个子序列在B中单调递增，它就是A的子序列。

哪个最长呢？当然是B的LIS最长。

自此完成转化。
'''
