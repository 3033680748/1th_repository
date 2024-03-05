n = int(input())
li = list(map(int,input().split()))

m = int(input())
com = []
for i in range(m):
    com.append(list(map(int,input().split())))

prefix_sum = [0 for _ in range(n)]

for i in range(n):
    if not i:
        prefix_sum[i] = li[i]
    else:
        prefix_sum[i] = prefix_sum[i-1]+li[i]

for down, up in com:
    down, up = down-1, up-1
    if down:
        out_ = prefix_sum[up] -prefix_sum[down-1]
    else:
        out_ = prefix_sum[up]
    print(out_)