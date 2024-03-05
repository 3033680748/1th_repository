'''
s[i][j] = s[i - 1][j] + s[i][j - 1] + a[i] [j] - s[i - 1][j - 1]
s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
'''

n = int(input())

matrix = [[0 for _ in range(n+1)]]

for i in range(n):
    matrix.append([0])
    for num in list(map(int, input().split())):
        matrix[i+1].append(num)

s = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j] = s[i-1][j] + s[i][j-1] + matrix[i][j] - s[i-1][j-1]


