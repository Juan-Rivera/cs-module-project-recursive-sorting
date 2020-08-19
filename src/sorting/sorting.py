# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_idx = 0
    arrB_idx = 0
    # Your code here
    for idx in range(elements):
        # checks if the index of the array (either A or B) is already at the end of the array 
        # and then uses the other array instead
        if arrA_idx >= len(arrA):
            # sets element in the merged array with the element from array B
            merged_arr[idx] = arrB[arrB_idx]
            # goes to next index in array B
            arrB_idx += 1

        elif arrB_idx >= len(arrB):
            # sets element in the merged array with the element from array A
            merged_arr[idx] = arrA[arrA_idx]
            # goes to next index in array A
            arrA_idx += 1

        # compares forst element of each array, stores smaller element in the new merged array
        elif arrA[arrA_idx] < arrB[arrB_idx]:
            # sets element in the merged array with the element from array A
            merged_arr[idx] = arrA[arrA_idx]
            # goes to next index in array A
            arrA_idx += 1

        else:
            # sets element in the merged array with the element from array B
            merged_arr[idx] = arrB[arrB_idx]
            # goes to next index in array B
            arrB_idx += 1
            
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
