class heap:
    def __init__(self):
        self.heap = []
        # in bytes
        self.heap = ["null"] * length

    def allocate_mem(self, memory):
        if not hasattr(self, "heap"):
            self.heap = []
        self.heap.extend(["null"] * memory)
        return memory

