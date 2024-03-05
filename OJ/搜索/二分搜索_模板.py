n, m = map(int, input().split())
num = list(map(int, input().split()))
q = list(map(int, input().split()))

num.sort()

for number in q:
    left = 0
    right = n-1
    check = -1
    while left <= right:
        mid = int((left+right)//2)
        if num[mid] == number:
            if num[mid-1] == number:
                right = mid
                continue
            else:
                check = 0
                print(mid+1,end=" ")
                break
        else:
            if num[mid] > number :
                right = mid - 1
            elif num[mid] < number :
                left = mid + 1
    if check == -1:
        print("-1",end=" ")
