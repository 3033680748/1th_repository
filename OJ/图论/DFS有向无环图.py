n = int(input())

mine = list(map(int, input().split()))

vis = [0 for _ in range(n+1)]
adjacency = [[] for _ in range(n+1)]

for i in range(1,n):
    temp = list(map(int, input().split()))
    for idx, num in enumerate(temp):
        if num == 1:
            adjacency[i].append(i+idx+1)
            #adjacency[i+idx+1].append(i)
# DFS+回溯
ans = 0
li_ans = []
def dfs(i,mines,track):
    if vis[i] != 0:
        return False
    else:
        vis[i] = 1
        mines += mine[i-1]
        track.append(i)
        check = 0
        for node in adjacency[i]:
            if dfs(node,mines,track) == False:
                check += 1
        if check == len(adjacency[i]):
            global ans,li_ans
            if ans < mines:
                ans = mines
                li_ans = track.copy()
            track.pop()
            vis[i] = 0
            return True
        track.pop()
        vis[i] = 0
        return True

for i in range(1,n+1):
    dfs(i,0,[])

for num in li_ans:
    print("{:d}".format(num),end=" ")

print("\r")
print(ans)