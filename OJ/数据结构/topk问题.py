import heapq
import random

li = [i for i in range(0,100,2)]

random.shuffle(li)

print(li)

k = 10

heap = []

for i in range(k):
    heap.append(li[i])

heapq.heapify(heap) # 小根堆

for i in range(k, len(li)):
    if heap[0] < li[i]:
        heap[0] = li[i]
        heapq.heapify(heap)
    else:
        continue

heap.reverse()

print(heap)