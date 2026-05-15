
from typing import List


class Heaps:
    def __init__(self):
        self.heap = []

    def heapify_up(self, i: int) -> None:
        while i > 0:
            parent = (i-1)//2
            if self.heap[parent] <= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
        # parent = (i-1)//2
        # while i>0 and self.heap[parent] > self.heap[i]:
        #     self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
        #     i = parent
        #     parent = (i-1)//2

    def heappush(self, num: int) -> None:
        self.heap.append(num)
        self.heapify_up(len(self.heap)-1)

    def heapify_down(self, i: int) -> None:
        left = 2*i + 1
        while left < len(self.heap):
            smallest = left
            right = 2*i + 2
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[i] <= self.heap[smallest]:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1

    def heappop(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            min_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify_down(0)
            return min_value

    def heapify(self, nums: List[int]) -> None:
        start = (len(nums) - 2)//2
        for i in range(start, -1, -1):
            self.heapify_down(i)






myHeap = Heaps()
# myHeap.heappush(3)
# myHeap.heappush(4)
# myHeap.heappush(5)
# myHeap.heappush(2)
print(myHeap.heap)
print(myHeap.heappop())
print(myHeap.heap)


