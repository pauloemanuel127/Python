#This program has a binary search function, an algorithm with the complexity equals O(logn)
#Realizes two test cases to test the algorithm

def binary_search(list, iten):
    """This function search for a specific element in a ordered list,
    the operation only occurs in a ordered list"""
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == iten:
            return mid
        if guess > iten:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 7))
print(binary_search(my_list, 2))
