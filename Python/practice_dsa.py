"""This module contains classes of different data structures"""

class Stack:
	"""Implements Stack via Python's inbuilt list data structure"""
	def __init__(self):
		self.stack = list()
		
	def push(self, element):
		self.stack.append(element)
	
	def pop(self):
		if not self.isEmpty():
			return self.stack.pop()
		return 'Stack is Empty'
	
	def peek(self):
		if not self.isEmpty():
			return self.stack[-1]
		return "Stack is Empty"
	
	def isEmpty(self):
		return self.size() == 0
	
	def size(self):
		return len(self.stack)

	
class Queue(Stack):
	
	def __init__(self):
		super().__init__()
		
	def enqueue(self, value):
		self.push(value)
	
	def dequeue(self):
		if not self.isEmpty():
			return self.stack.pop(0)
		return 'Stack is Empty'
	
	def peek(self):
		if not self.isEmpty():
			return self.stack[0]
		return "Stack is Empty"
	
	def traverse(self):
		if not self.isEmpty():
			print('Traversing through the Queue:')
			for num in self.stack:
				print(num, end = " -> ")
		else:
			return "Stack is Empty"


class Node:
	"""Implements the node"""
	def __init__(self, value):
		self.value = value
		self.next = None


class StackViaLL:
	"""Implementing the stack via the Linked List"""
	def __init__(self):
		self.head = None
		self.size = 0
		
	def push(self, value):
		new_node = Node(value)
		if self.head:
			new_node.next = self.head
		self.head = new_node
		self.size += 1
	
	def peek(self):
		if not self.isEmpty:
			return self.head.value
		return 'The List is Empty'
	
	def pop(self):
		if not self.isEmpty():
			popped_element = self.head
			self.head = self.head.next
			self.size -= 1
			return popped_element.value
		return 'The List is Empty'
	
	def isEmpty(self):
		return self.size == 0
	
	def sizes(self):
		return self.size

	def traverse_stack(self):
		if not self.isEmpty():
			print('Traversing through the stack:\n')
			current_node = self.head
			while current_node:
				print(current_node.value, end = " -> ")
				current_node = current_node.next
		else:
			return 'The List is Empty'


class QueueViaLL:
	
	def __init__(self):
		self.head = None
		self.first = None
		self.size = 0
	
	def enqueue(self, value):
		new_node = Node(value)
		if not self.head:
			self.first = new_node
		if self.head:
			self.head.next = new_node
		self.head = new_node
		self.size += 1
	
	def isEmpty(self):
		return self.size == 0
		
	def dequeue(self):
		if not self.isEmpty():
			if self.size == 1:
				self.first, self.head = None, None
				self.size = 0
			else:
				removed = self.first
				self.first = self.first.next
				self.size -= 1
		else:
			return print("The Queue is Empty")
	
	def traverse(self):
		"""Traversing through all the elements in the Queue"""
		if not self.isEmpty():
			if not self.size == 1:
				current_node = self.first
				print('Traversing through the Queue')
				while current_node:
					print(current_node.value, end = " -> ")
					current_node = current_node.next
				print("None")
			else:
				print("Traversing through the queue")
				print(self.first.value)
		else:
			return print("The Queue is empty")

	def peek(self):
		if not self.isEmpty():
			return self.first.value
		return "The Queue is empty"

			
			
