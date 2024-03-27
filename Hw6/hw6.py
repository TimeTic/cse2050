def bubble_sort(arr, n=None, num_swaps=0):
    """
    Sorts an array using the recursive Bubble Sort algorithm.

    Parameters:
        arr (list): The unsorted list to be sorted.
        n (int, optional): The length of the unsorted portion of the array. 
            Defaults to None, which implies the entire array length.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr, num_swaps
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]  # corrected typo here
            num_swaps += 1
    return bubble_sort(arr, n-1, num_swaps)


def selection_sort(arr, end=None, num_swaps=0):
    """
    Sorts an array using the recursive Selection Sort algorithm based on the largest element each time.

    Parameters:
        arr (list): The unsorted list to be sorted.
        end (int): The index up to which the sorting process is done.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    if end is None:
        end = len(arr) - 1

    if end <= 0:
        return arr, num_swaps

    max_index = 0
    for i in range(1, end + 1):
        if arr[i] > arr[max_index]:
            max_index = i

    if max_index != end:
        arr[end], arr[max_index] = arr[max_index], arr[end]
        num_swaps += 1

    return selection_sort(arr, end - 1, num_swaps)

def insertion_sort(arr, n=None, num_swaps=0):
    """
    Sorts an array using the recursive Insertion Sort algorithm.

    Parameters:
        arr (list): The unsorted list to be sorted.
        n (int, optional): The length of the unsorted portion of the array. 
            Defaults to None, which implies the entire array length.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    if n is None:
        n = len(arr)

    if n <= 1:
        return arr, num_swaps
    
    sorted_arr, num_swaps =  insertion_sort(arr, n-1, num_swaps)
    last = arr[n - 1]
    j = n-2
    while j >= 0 and last < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
        num_swaps += 1
        arr[j + 1] = last

    return arr, num_swaps


# Testing code
sort_list = [i for i in range(5)]
sorted_arr, n_swaps = bubble_sort(sort_list) 
print(n_swaps)

rev_sorted = [i for i in range(5,0,-1)]
sorted_arr, n_swaps = bubble_sort(rev_sorted)
print(n_swaps)

random_list = [3, 2, 5, 1, 4]
sorted_arr, n_swaps = bubble_sort(random_list)
print(n_swaps)
