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
