
class Heap():
    def sift(self,li,low,high):
        i = low
        j = i*2 + 1
        tmp = li[low]
        while j <= high:
            if j + 1 <= high and li[j+1] < li[j]:
                j += 1
            if tmp > li[j]:
                li[i] = li[j]
                i = j
                j = 2*i + 1
            else:
                li[i] = tmp
                break
        else:
            li[i] = tmp

    def heap_build(self,li):
        n = len(li)
        for i in range((n-2)//2,-1 , -1):
            self.sift(li, i, n -1)

    def heap_sort(self, li):
        self.heap_build(li)
        n = len(li)
        for i in range(n - 1, -1, -1):
            li[0],li[i] = li[i], li[0]
            self.sift(li, 0, i -1)

    def op1(self, li, x):
        li.append(x)

    def op2(self, li):
        n = len(li)
        self.sift(li, 0, n-1)
        print(li[-1])

    def op3(self, li):
        n = len(li)
        self.sift(li, 0 , n -1)
