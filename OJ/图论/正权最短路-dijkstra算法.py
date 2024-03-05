'''
经过不严谨的证明，heapify会自动设置索引直到取得单一的int/float对象，并将这个对象作为操作key值，但是要保证所有的索引层数一致
如果索引层数不一致:
TypeError: '<' not supported between instances of 'int' and 'list'
'''

n = 7

# 邻接表
adjacency = [
    [[4,1],[2,2]],
    [[4,3],[5,10]],
    [[1,4],[6,5]],
    [[3,2],[6,8],[7,4],[5,2]],
    [[7,1]],
    [],
    [[6,1]]
]

dist = [99999 for _ in range(n)]

path = [0 for _ in range(n)]

from heapq import heapify

my_heap = []

# 将起点定为v3

dist[2] = 0

my_heap.append([dist[2],3])

while len(my_heap):
    heapify(my_heap)
    curNode = my_heap[0][1]
    curDist = dist[curNode-1]
    if adjacency[curNode-1] != []:
        for vector in adjacency[curNode - 1]:
            path_ = curDist + vector[1]
            if path_ < dist[vector[0]]:
                my_heap.append([path_, vector[0]])
    my_heap.pop(0)

