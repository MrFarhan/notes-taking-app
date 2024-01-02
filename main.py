from flask import Flask, jsonify, request
from flask_cors import CORS
from server.stack_class import Stack
from server.linked_list_class import LinkedList
from server.queue_class import Queue

app = Flask(__name__)
CORS(app)


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
