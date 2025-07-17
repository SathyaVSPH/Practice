
class DSAsearch:
	'''This module contains different types of searching funtions'''
	
	def __init__(self, arr):
		self.arr = sorted(arr)
	
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

	def interpolation_search(self, target):
		low, high = 0, len(self.arr) - 1

		while low <= high and self.arr[low] <= target and self.arr[high] >= target:

			if self.arr[low] == self.arr[high]:
				if self.arr[low] == target:
					return low
				else:
					return -1
			
			mid = low + ((target - self.arr[low]) * (high - low)) // (self.arr[high] - self.arr[low])

			if self.arr[mid] == target:
				return mid
			elif self.arr[mid] < target:
				low = mid + 1
			else:
				high = mid - 1
		
		return -1
