class Stack():
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if len(self.stack) <= 0:
            return None
        else:
            self.stack.pop()
    def gettop(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[-1]

# 判断括号合理性问题

bracket_check = Stack()

List = input()

n = len(list)

for i in range(n):
    if List[i] == '(' or List[i] == '[' or List[i] == '{':
        bracket_check.push(List[i])
    else:
        bracket_check.pop()

Bool = (len(List) == 0)

