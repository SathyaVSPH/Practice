
class DSAsearch:
	'''This module contains different types of searching funtions'''
	
	def __init__(self, arr):
		self.arr = arr
	
	def linear_search(self, target):
		'''To search for the target in the array linearly'''
		for i in range(len(self.arr)):
			if self.arr[i] == target:
				return i
		return -1

	def binary_search(self, target):
		self.arr.sort()
		left = 0
		right = len(self.arr)-1
		
		while (left<=right): #don't forget to include =. very important
			mid = (left + right)//2
			if self.arr[mid] == target:
				return mid
			elif self.arr[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		
		return -1 #Not found

