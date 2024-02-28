# Searching and sorting 
#practice
def binary_search(L, item):
    """returns trie if and only if item is in the sorted list L.
    returns false otherwise.
    """
    # Base Case empty list
    if len(l) == 0:
        return False
    
    # get the middle index

    mid = len(L) // 2

    #see if middle item is item I'm loooking for
    if item == L[mid]:
        return True
    