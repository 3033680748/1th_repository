'''
class Heap(): #大根堆
    def sift(self,li,low,high):
        """

        :param li: 待排序列表
        :param low: 堆的根节点
        :param high: 堆的最后一个元素的位置
        :return:
        """
        i= low
        j = 2 * i + 1#左侧子节点
        tmp = li[low] #存堆顶
        while j <= high:
            if j + 1 <= high and li[j + 1] > li[j]:
                j = j + 1 #指向右侧子节点
            if tmp < li[j]:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                li[i] = tmp
                break
        else:
            li[i] = tmp
    def heap_build(self, li):
        n = len(li)
        for i in range((n-2)//2, -1, -1):
            self.sift(li, i, n-1)

    def heap_sort(self,li):
        n = len(li)
        for i in range(n-1, -1, -1):
            # i指向最后的一个元素
            li[0], li[i] = li[i], li[0]
            self.sift(li, 0, i-1)



lister = [i for i in range(100)]

import random

random.shuffle(lister)

HEAP = Heap()

HEAP.heap_build(lister)

HEAP.heap_sort(lister)

print(lister)
'''

import heapq

import random

li = [i for i in range(10)]

# print(li)

random.shuffle(li)

heapq.heapify(li)

print(li)

for i in range(len(li)):
    print(li[0], end= ' ')
    heapq.heappop(li)

