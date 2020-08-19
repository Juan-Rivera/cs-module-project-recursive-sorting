# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
    # Your code here
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1
    elif low > high:
        return -1 # not found
    elif arr[middle] == target:
        return middle
    else:
        if target < arr[middle]:
            high = middle-1
        else:      
            low = middle+1
        return binary_search(arr, target, low, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):

    low = 0
    high = len(arr)-1
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1
    # checking if the target equals the middle
    if arr[middle] == target:
        print(middle)
        return middle
    
    else: 
        # target is greater
        if target > arr[middle]:
            one_half = arr[middle:high + 1]
        # target is less
        elif target < arr[middle]:
            one_half = arr[low:middle + 1]
        print(one_half)
        # goes through the binary search again (recursively) and the new array is the half that we took from above
        return agnostic_binary_search(one_half, target)