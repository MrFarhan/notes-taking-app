class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def delete(self):
            queue_copy = Queue()
            queue_copy.dequeue()
            deleted_note = self.dequeue()
            return deleted_note
        
    def bubble_sort(self):
        queue_items = []
        while not self.is_empty():
            queue_items.append(self.dequeue())

        n = len(queue_items)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if queue_items[j] > queue_items[j + 1]:
                    queue_items[j], queue_items[j + 1] = queue_items[j + 1], queue_items[j]

        for item in queue_items:
            self.enqueue(item)