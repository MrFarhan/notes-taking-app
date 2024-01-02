
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)
        
    def delete_by_index(self):
            stack_copy = Stack()
            stack_copy.pop()
            deleted_note = self.pop()
            return deleted_note
        
    def bubble_sort(self):
        stack_items = []
        while not self.is_empty():
            stack_items.append(self.pop())

        n = len(stack_items)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if stack_items[j] > stack_items[j + 1]:
                    stack_items[j], stack_items[j + 1] = stack_items[j + 1], stack_items[j]

        for item in stack_items[::-1]:
            self.push(item) 