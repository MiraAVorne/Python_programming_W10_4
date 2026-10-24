########################################################
# Task A10_T4
# Developer Sami Viljanen
# Date 2025-10-27
########################################################


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    
    # Merge two sorted subarrays into a single sorted array.
     
    # Initialize pointers for left (i), right (j), and merge (k) arrays
    i = j = k = 0
    
    # Compare elements from both arrays and merge in sorted order
    while i < len(PLeft) and j < len(PRight):

        if PAsc:  # Ascending order
            if PLeft[i] <= PRight[j]:
                PMerge[k] = PLeft[i]
                i += 1
            else:
                PMerge[k] = PRight[j]
                j += 1

        else:  # Descending order
            if PLeft[i] >= PRight[j]:
                PMerge[k] = PLeft[i]
                i += 1
            else:
                PMerge[k] = PRight[j]
                j += 1
        k += 1

    # Copy remaining elements from left array (if any)
    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    # Copy remaining elements from right array (if any)
    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1

    return None


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    
    # Sort an array using the merge sort algorithm (divide-and-conquer).
    
    n = len(PValues)
    
    # Base case: arrays with 0 or 1 element are already sorted
    if n <= 1:
        return
    
    # Divide: split array into two halves
    mid = n // 2
    left = PValues[:mid]
    right = PValues[mid:]

    # Conquer: recursively sort both halves
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    # Combine: merge the sorted halves back into original array
    merge(left, right, PValues, PAsc)
    return None
