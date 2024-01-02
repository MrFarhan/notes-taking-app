from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

    def delete_by_index(self):
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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def display(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)
            print(current.data, end=' ')
            current = current.next
        return nodes
    
    
    def delete_last_node(self):
        if not self.head:
            return False  # Empty list, nothing to delete

        if not self.head.next:
            self.head = None  # Only one node in the list
            return True

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None  # Set the next of the second-to-last node to None
        return self.display()
    
    
    def bubble_sort(self):
        if not self.head:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    # Swap nodes
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next


notes_stack = Stack()
notes_queue = Queue()
notes_sort = LinkedList()

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.json.get('note')
    if note:
        notes_stack.push(note)
        notes_queue.enqueue(note)
        notes_sort.append(note)
        return jsonify({'message': 'Note added successfully!'}), 200
    return jsonify({'error': 'Note could not be added.'}), 400

@app.route('/view_notes', methods=['GET'])
def view_notes():
    notes_sort.bubble_sort()
    notes_from_stack = list(notes_stack.items)
    notes_from_queue = list(notes_queue.items)
    notes_from_sort = list(notes_sort.display())
    return jsonify({'stack_notes': notes_from_stack, 'queue_notes': notes_from_queue, 'sort_notes': notes_from_sort}), 200

@app.route('/delete_note/stack', methods=['DELETE'])
def delete_stack_note():
    deleted_note = notes_stack.delete_by_index()
    if deleted_note is not None:
        return jsonify({'message': f'Note deleted successfully from Stack: {deleted_note}'}), 200
    return jsonify({'error': 'Invalid index or no notes present in Stack.'}), 400

@app.route('/delete_note/queue', methods=['DELETE'])
def delete_queue_note():
    deleted_note = notes_queue.delete_by_index()
    if deleted_note is not None:
        return jsonify({'message': f'Note deleted successfully from Queue: {deleted_note}'}), 200
    return jsonify({'error': 'Invalid index or no notes present in Queue.'}), 400

@app.route('/delete_note/sort', methods=['DELETE'])
def delete_sort_note():
    deleted_note = notes_sort.delete_last_node()
    if deleted_note is not None:
        return jsonify({'message': f'Note deleted successfully from Stack: {deleted_note}'}), 200
    return jsonify({'error': 'Invalid index or no notes present in Stack.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
