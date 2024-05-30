class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert_key(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.min_heapify(0)

        return root

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

# Usage
heap = MinHeap()
heap.insert_key(3)
heap.insert_key(2)
# heap.delete_key(1)
heap.insert_key(15)
heap.insert_key(5)
heap.insert_key(4)
heap.insert_key(45)

print(heap.heap)
# print(heap.extract_min())
heap.delete_key(1)

print(heap.heap)
# print(heap.extract_min())
# print(heap.extract_min())
# print(heap.extract_min())
# print(heap.extract_min())
# print(heap.extract_min())






