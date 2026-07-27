#This program has a binary search function, an algorithm with a complexity of O(log(n))

def binary_search(array, item):
    """
    This function receives a sorted array and an item to search for.
    Returns the index of the value, or None if it isn't in the array.
    """

    low = 0
    high = len(array) - 1

    while low <= high:

        mid = int((low + high) / 2)
        guess = array[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None