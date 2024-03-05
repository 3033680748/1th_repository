# queue先进先出

class queue:
    def __init__(self, length):
        self.queue = [None for _ in range(length)]
        self.length = length
        self.rear = 0 # 队尾，进队，指向的位置应该为空
        self.front = 0 # 队首，出队，指向的位置应该为对列的最前端一个数

    def is_full(self)->bool:
        if (self.rear + 1) % self.length == self.front:
            return True
        else:
            return False
    def is_empty(self)->bool:
        if self.front == self.rear:
            return True
        else:
            return False
    def push(self, number):
        if self.is_full() == True:
            print("queue is full now")
        else:
            self.rear = (self.rear + 1) % self.length
            self.queue[self.rear] = number


    def pop(self):
        if self.is_empty() == True:
            print("queue is empty now")
        else:
            self.front = (self.front + 1) % self.length
            self.queue[self.front] = None


a = queue(5)
a.push(8)
a.pop()
print(a.queue)

# 直接碉堡
from collections import deque
b = deque([0,3,4], 5)
b.append(1)# 队尾进队
b.popleft()# 队首出队

b.appendleft(2) # 队首进队
b.pop() # 队尾出队