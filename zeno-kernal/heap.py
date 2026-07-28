class heap:
    def __init__(self):
        self.heap = []

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] <= self.heap[index]:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def _sift_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = left + 1
            smallest = index

            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")

        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def allocate_mem(self, memory, req_mem):
        if req_mem < 0:
            raise ValueError("request size cannot be negative")
        if not hasattr(self, "heap"):
            self.heap = []
        self.heap.extend([None] * memory)
        return memory

