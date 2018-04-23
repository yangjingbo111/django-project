# build the full list in memory
# def firstn(n):
# 	num, nums = 0, []
# 	while num < n:
# 		nums.append(num)
# 		num += 1
# 	return nums

# sum_of_first_n = sum(firstn(1000000))
# print(sum_of_first_n)


# using the generator pattern (an iterable)
# class firstn(object):
# 	def __init__(self, n):
# 		self.n = n
# 		self.num, self.nums = 0, []

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		if self.num < self.n:
# 			cur, self.num = self.num, self.num+1
# 			return cur
# 		else:
# 			raise StopIteration()

# sum_of_first_n = sum(firstn(1000000))
# print(sum_of_first_n)

# a generator that yields items instead of returning a list
def firstn(n):
	num = 0
	while num < n:
		yield num
		num += 1
print(firstn(1000000))
# print(sum_of_first_n)