# Write a python program to create a list and use the following functions-
# •
# append() and extend()
# •
# len()

# 1 Using append
print("Using append")
a = [10, 12, 13, 17]

# appending multiple values
a.append(20)
a.append(22)
print(a)


# 2 Using extend
print("Using extend")
# Creating a list
list = ['1','2','3']
for l in list:  # Iterating list
    print(l)
list.extend('4')
print("After extending:")
for l in list:  # Iterating list
    print(l)

print("method2")

a = [10, 12, 13, 17]

b = [30, 40]

a.extend(b)

print(a)


#3 Using len
print("Using len")

# Function which return length of string
def findLength(string):

	# Initialize count to zero
	count = 0

	# Counting character in a string
	for i in string:
		count += 1
	# Returning count
	return count


# Driver code
string = "geeksforgeeks"
print(findLength(string))
