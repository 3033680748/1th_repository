n, m = map(int, input().split())

maze = []

MOD = int(1e9+7)

for _ in range(n):
    temp = input()
    temp = temp.replace('.','1')
    temp = temp.replace('X','0')
    temp = int(temp,2)
    maze.insert(0,temp)

max_ = '1'
for _ in range(m-1):
    max_ += '1'

max_ = int(max_,2)

maze.insert(0,max_)


dp = [[ 0 for j in range(max_+1)] for i in range(n+1)]

dp[0][max_] = 1
def check1(num,i):
    if (num|maze[i]) == maze[i]:
        num = (bin(num))[2:]
        beg = 0
        end = len(num)
        for _ in range(len(num)):
            if num[_] == '1':
                beg = _
                break
        for _ in range(beg,len(num)):
            if num[_] == '0':
                end = _
                break
        for _ in range(end,len(num)):
            if num[_] == '1':
                return False
        return True
    else:
        return False

def check2(num1,num2):
    if (num1&num2) == num1:
        return True
    else:
        return False
 
for i in range(1,n+1):
    for j in range(0,max_+1):
        for k in range(0,max_+1):
            if check1(k,i-1) and check1(j,i) and check2(j,k):
                dp[i][j] += dp[i-1][k]
                
        
ans = sum(dp[n])

print(ans)
