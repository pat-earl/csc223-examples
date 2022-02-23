def min_max(l):
    """
    Description: bla b
    Parameters: l - list
    Return Values: 
            smallest - 
            largest - 
    """
    smallest = l[0]
    largest = l[0]

    for item in l:
        if item < smallest:
            smallest = item
        elif item > largest:
            largest = item

    return smallest, largest

(small, large) = min_max([2, 3, 4, -1, 10, 9, 8])
print(small)
print(large)