"""Implementing Linked List"""

class Node:
    """Instantiating a node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Linked_List:
    """Instantiating a Linked List"""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Adds the new element to the end"""
        new_node = Node(data)
        
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        else:
            self.head = new_node
        self.size += 1
        return f'{data} is appended at the end.'

    def print(self):
        """Prints all the elements in the Linked List"""
        if not self.head:
            return print("The Linked List is empty")
        
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print('None')
    
    def insert(self, index, data):
        """Inserts the element at the specified index"""
        if not self.head:
            return self.append(data)
        
        current = self.head
        current_idx = 0
        while current:
            if current_idx == index - 1:
                temp = current.next
                current.next = Node(data)
                current.next.next = temp
                current_idx += 1
                return f'inserted the {data} at index {index}.'
            current = current.next
            current_idx += 1
        return f'Index {index} is invalid'

    def delete(self, data):
        """Deletes the data from the Linked List"""
        if not self.head:
            return 'The Linked List is Empty'
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return f'Deleted {data}'
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return f'Deleted {data}'
            current = current.next
        return 'Not found'
                

ll = Linked_List()
print(ll.append(10))
ll.append(20)
ll.print()
print(ll.insert(1, 15))
ll.print()
print(ll.delete(0))
ll.print()
