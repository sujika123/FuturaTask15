# Write a python program to print maximum and minimum number in a tuple.

t = (25, 17, 55, 63, 40, 32)

max_val = t[0]

for i in range(len(t)):
	if t[i] > max_val:
		max_val = t[i]

print("Maximum value is:", max_val)


min_val = t[0]

for i in range(len(t)):
	if t[i] < min_val:
		min_val = t[i]

print("Minimum value is:", min_val)