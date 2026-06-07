# Selection Sort algorithm, has a worst-case time complexity of O(n²).
# For this algorithm I used two functions. 
# The first one searches for the smallest value in the array and returns the value's index.
# The second one adds the values in order, one by one, to a new array and returns the new array.

def  smallest_search(array):
    """
    This function receives an array, searches for the smallest value, and returns its index.
    """
    
    smallest =  array[0]
    smallest_value_index = 0
    
    for i in range(1, len(array)):

        if array[i] < smallest:
            smallest = array[i]
            smallest_value_index = i

    return smallest_value_index

def selection_sort(array):
    """
    This function receives an array, sorts the elements one by one using the 
    smallest_search function to find the values, and returns a new sorted array.
    """
    new_array = []

    for i in range(len(array)):

        smallest = smallest_search(array)
        new_array.append(array.pop(smallest))

    return new_array