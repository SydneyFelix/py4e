def square(nums):
	lst = []
	for i in nums:
		lst.append(i*i)
	return lst

my_nums = square([1,2,3])


print(my_nums)
print('**************')
print(my_nums[0])
print('**************')
print(my_nums[1])
print('**************')
print(my_nums[2])

n = 0
for i in my_nums:
	print('**************')
	print(my_nums[n])
	n+=1
