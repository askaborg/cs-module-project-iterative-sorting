def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # let's figure out the total size of the arr 
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # find the midpoint 
        mid = (left + right) // 2

        # check if the midpoint is the target
        if arr[mid] == target:
            return mid 
        
        # check if the element should be left or right
        if arr[mid] < target:
            # throw out the left side of the arr 
            left = mid + 1

        # otherwise, arr[mid] > target 
        else:
            # throw out the right side of the arr
            right = mid - 1

    return -1  # not found
