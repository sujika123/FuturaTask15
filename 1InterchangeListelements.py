# Python program to interchange first and last elements in a list.

# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


print("_______________________")
#Method 2

# Swap function
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))