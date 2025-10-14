import practice_dsa as dsa

'''stack1 = dsa.StackViaLL()
print(stack1.pop())
print(stack1.peek())
print(stack1.push(1))
for num in [2,3,4,5]:
	print(stack1.push(num))
print(stack1.pop())
print(stack1.peek())
print(stack1.sizes())
print(stack1.traverse_stack())
'''

'''queue1 = dsa.Queue()
print(queue1.dequeue())
print(queue1.peek())
print(queue1.enqueue(1))
for num in [2,3,4,5]:
	print(queue1.enqueue(num))
print(queue1.dequeue())
print(queue1.size())
print(queue1.traverse())'''

queue1 = dsa.QueueViaLL()
queue1.dequeue()
queue1.enqueue(3)
queue1.enqueue(4)
queue1.traverse()
print(queue1.peek())