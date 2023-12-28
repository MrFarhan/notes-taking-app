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
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)
        
    def delete_by_index(self, index):
        if 0 < index and index <= self.size():
            stack_copy = Stack()
            for _ in range(self.size() - index):
                stack_copy.push(self.pop())
            deleted_note = self.pop()
            while not stack_copy.is_empty():
                self.push(stack_copy.pop())
            return deleted_note
        return None    
        
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
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def delete_by_index(self, index):
        if 0 < index and index <= self.size():
            queue_copy = Queue()
            for _ in range(self.size() - index):
                queue_copy.enqueue(self.dequeue())
            deleted_note = self.dequeue()
            while not queue_copy.is_empty():
                self.enqueue(queue_copy.dequeue())
            return deleted_note
        return None
        
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


notes_stack = Stack()
notes_queue = Queue()

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.json.get('note')
    if note:
        notes_stack.push(note)
        notes_queue.enqueue(note)
        return jsonify({'message': 'Note added successfully!'}), 200
    return jsonify({'error': 'Note could not be added.'}), 400

@app.route('/view_notes', methods=['GET'])
def view_notes():
    notes_from_stack = list(notes_stack.items[::-1])
    notes_from_queue = list(notes_queue.items)
    return jsonify({'stack_notes': notes_from_stack, 'queue_notes': notes_from_queue}), 200

# @app.route('/delete_note/<int:index>', methods=['DELETE'])
# def delete_note(index):
#     if not notes_stack.is_empty() and not notes_queue.is_empty():
#         deleted_note_stack = notes_stack.delete_by_index(index)
#         deleted_note_queue = notes_queue.delete_by_index(index)
#         if deleted_note_stack and deleted_note_queue:
#             return jsonify({'message': f'Note deleted successfully from Stack and Queue: {deleted_note_stack}'}), 200
#     return jsonify({'error': 'Invalid index or no notes present.'}), 400

@app.route('/delete_note/stack/<int:index>', methods=['DELETE'])
def delete_stack_note(index):
    deleted_note = notes_stack.delete_by_index(index + 1)
    if deleted_note is not None:
        return jsonify({'message': f'Note deleted successfully from Stack: {deleted_note}'}), 200
    return jsonify({'error': 'Invalid index or no notes present in Stack.'}), 400

@app.route('/delete_note/queue/<int:index>', methods=['DELETE'])
def delete_queue_note(index):
    deleted_note = notes_queue.delete_by_index(index + 1)
    if deleted_note is not None:
        return jsonify({'message': f'Note deleted successfully from Queue: {deleted_note}'}), 200
    return jsonify({'error': 'Invalid index or no notes present in Queue.'}), 400



if __name__ == '__main__':
    app.run(debug=True)
