n = int(input())

insert = []

for _ in range(n-1):
    insert.append(list(map(int, input().split())))

m = int(input())

delete = []

for _ in range(m):
    delete.append(int(input()))

class node(object):
    def __init__(self,val,pre,aft):
        self.val = val
        self.pre = pre
        self.aft = aft

Node_1 = node(1,None,None)

for index,com in enumerate(insert):
    p1 = Node_1
    while p1:
        check = p1.val
        if check == com[0]:
            break
        else:
            p1 = p1.pre
    if p1 and p1.val == com[0]:
        if com[1] == 1: # 右插
            p2 = p1.aft
            p1.aft = node(index+2,p1,p2)
            if p2 :
                p2.pre = p1.aft
        else: #左插
            p2 = p1.pre
            p1.pre = node(index+2,p2,p1)
            if p2:
                p2.aft = p1.pre
    else:
        p1 = Node_1
        while p1:
            check = p1.val
            if check == com[0]:
                break
            else:
                p1 = p1.pre
        if p1 and p1.val == com[0]:
            if com[1] == 1:  # 右插
                p2 = p1.aft
                p1.aft = node(index + 2, p1, p2)
                if p2:
                    p2.pre = p1.aft
            else:  # 左插
                p2 = p1.pre
                p1.pre = node(index + 2, p2, p1)
                if p2:
                    p2.aft = p1.pre

for com in delete:
    p1 = Node_1
    while p1 :
        check = p1.val
        if check == com:
            break
        else:
            p1 = p1.pre
    if p1 and p1.val == com:
        p0 = p1.pre
        p2 = p1.aft
        p0.aft = p2
        p2.pre = p0
    else:
        p1 = Node_1
        while p1:
            check = p1.val
            if check == com:
                break
            else:
                p1 = p1.pre
        if p1 and p1.val == com:
            p0 = p1.pre
            p2 = p1.aft
            p0.aft = p2
            p2.pre = p0

head = Node_1
while head.pre :
    head = head.pre

tail = head
while tail.aft:
    print(tail.val,end=" ")
    tail = tail.aft

print(tail.val)