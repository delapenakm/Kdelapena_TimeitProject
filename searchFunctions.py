def binary_search(mylist : list, find : int) -> int:
    """Function that uses binary search to find a specific value in a list"""

    # Establish lowest index value (0) and highest index value (length of list)
    low = 0
    high = len(mylist) - 1

    # Search until no halves left to search
    while low <= high:
         # Establish middle index and value at that index
         middlePosition = (high + low) // 2
         middleNumber = mylist[middlePosition]

        # Return position if find is equal to the number at that position
         if find == middleNumber:
             return middlePosition
         # If find is less than middle value, look at left half of list
         elif find < middleNumber:
             high = middlePosition - 1
        # If find is greater than middle value, look at right half of list
         else: 
             low = middlePosition + 1

    # Return -1 if number is not found
    return -1


#---------------------------\
def linear_search(mylist : list, find : int) -> int:
    """Function that uses linear search to find a number in a list"""

    # Set currentPosition equal to 0 and set max position to highest possible index value
    # which is length of list - 1
    currentPosition = 0
    maxPosition = len(mylist) - 1

    # Continue iteration through loop until all numbers searches
    while currentPosition <= maxPosition:
        currentNumber = mylist[currentPosition]

        # If find is found, return its position
        if currentNumber == find:
            return currentPosition

        # Add 1 to position to search next value
        currentPosition += 1

    # Return -1 if not found
    return -1


def interpolation_search(mylist : list, find : int) -> int:
    low = 0
    high = len(mylist) - 1

    while low <= high and find >= mylist[low] and find <= mylist[high]:
        if mylist[low] == mylist[high]:
            if mylist[low] == find:
                return low

            return -1

        pos = low + int(
            (find - mylist[low]) * (high - low) / (mylist[high] - mylist[low])
        )

        posNumber = mylist[pos]

        if posNumber == find:
            return pos
        elif find < posNumber:
            high = pos - 1
        else:
            low = pos + 1


    return -1