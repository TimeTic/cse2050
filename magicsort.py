from enum import Enum
import math

class MagicCase(Enum):
    SORTED = 1
    CONSTANT_NUM_INVERSIONS = 2
    REVERSE_SORTED = 3
    GENERAL = 4

INVERSION_BOUND = 10

def linear_scan(L):
    if L == sorted(L):
        return MagicCase.SORTED
    elif L == sorted(L, reverse=True):
        return MagicCase.REVERSE_SORTED
    elif sum(L[i-1] > L[i] for i in range(1, len(L))) < INVERSION_BOUND:
        return MagicCase.CONSTANT_NUM_INVERSIONS
    else:
        return MagicCase.GENERAL

def reverse_list(L):
    left, right = 0, len(L) - 1
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def magic_insertionsort(L, left, right):
    for i in range(left + 1, right):
        key = L[i]
        j = i - 1
        while j >= left and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

def magic_mergesort(L, left, right):
    if right - left <= 20:
        magic_insertionsort(L, left, right)
    else:
        mid = (left + right) // 2
        magic_mergesort(L, left, mid)
        magic_mergesort(L, mid, right)
        merge(L, left, mid, right)

def merge(L, left, mid, right):
    left_part = L[left:mid]
    right_part = L[mid:right]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            L[k] = left_part[i]
            i += 1
        else:
            L[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        L[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        L[k] = right_part[j]
        j += 1
        k += 1

def magic_quicksort(L, left, right, depth=0):
    if depth > 2 * math.log2(len(L)) + 1:
        magic_mergesort(L, left, right)
        return
    if right - left <= 20:
        magic_insertionsort(L, left, right)
        return
    if left < right:
        pivot_index = partition(L, left, right)
        magic_quicksort(L, left, pivot_index, depth + 1)
        magic_quicksort(L, pivot_index + 1, right, depth + 1)

def partition(L, left, right):
    pivot = L[right - 1]
    i = left - 1
    for j in range(left, right - 1):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[right - 1] = L[right - 1], L[i + 1]
    return i + 1

def magicsort(L):
    result = set()
    case = linear_scan(L)
    if case == MagicCase.SORTED:
        return result
    elif case == MagicCase.REVERSE_SORTED:
        reverse_list(L)
        result.add('reverse_list')
    elif case == MagicCase.CONSTANT_NUM_INVERSIONS:
        magic_insertionsort(L, 0, len(L))
        result.add('magic_insertionsort')
    else:
        magic_quicksort(L, 0, len(L))
        result.add('magic_quicksort')
    return result
