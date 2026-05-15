
from typing import List


class Heaps:
    def __init__(self):
        self.heap = []

    def heapify_up(self, i: int) -> None:
        while i>0:
            parent = (i-1)//2
            if self.heap[parent] >= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def heappush(self, num: int) -> None:
        self.heap.append(num)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, i: int) -> None:
        left = 2*i + 1
        while left < len(self.heap):
            right = 2*i + 2
            greater = left
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                greater = right

            if self.heap[i] >= self.heap[greater]:
                break

            self.heap[i], self.heap[greater] = self.heap[greater], self.heap[i]

            i = greater
            left = 2*i + 1

    def heappop(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return max_value

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        start = (len(self.heap) - 2)//2
        for i in range(start, -1, -1):
            self.heapify_down(i)







myHeap = Heaps()
myHeap.heappush(1)
myHeap.heappush(2)
myHeap.heappush(3)
myHeap.heappush(5)
myHeap.heappush(6)
print(myHeap.heap)
print(myHeap.heappop())
print(myHeap.heappop())
print(myHeap.heap)


