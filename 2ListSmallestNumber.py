#Python program to find smallest number in a list.

print("Method 1")

list = [15, 25, 3, 13, 57, 100, 2, 128]
print(list)
smallest_num = list[0]

for i in list:
    if i < smallest_num:
        smallest_num = i

print("the smallest number in this list is:", smallest_num)



print("__________________")
print("Method 2")

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the first element
print("Smallest element is:", list1[0])



print("__________________")

# Method 3
print("Method 3")

# list of numbers
list1 = [10, 20, 1, 45, 99]

# printing the minimum element
print("Smallest element is:", min(list1))