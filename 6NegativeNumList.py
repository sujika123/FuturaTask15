# Write a python program to print negative numbers in a list.


# list of numbers
list1 = [-10, 21, -4, 0, -45, -66, 93]
num = 0

# using while loop
while (num < len(list1)):

	# checking condition
	if list1[num] < 0:
		print(list1[num], end=" ")

	# increment num
	num += 1