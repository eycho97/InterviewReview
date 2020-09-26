from typing import Iterable
from AuxiliaryMethods import *
import random
"""
Lecture 5 Sorting
"""


# Selection Sort
# O(n^2)
def selectionSort(A: Iterable[int], lo: int, hi: int) -> None:
    """
    Implementation of selection sort
    requires 0 <= lo and lo <= hi and hi <= len(A)
    ensures isSorted(A, lo, hi)
    """
    for i in range(hi):
        assert lo <= i and i <= hi
        assert isSorted(A, lo, i)
        assert leSegs(A, lo, i, A, i, hi)
        min = findMin(A, i, hi)
        swap(A, i, min)


A = [1,5,6,7,3,4]
print(A)
selectionSort(A, 0, len(A))
print(A)

# Best & Average: O(nlogn) Worst: O(n^2)
def partition(A: Iterable[int], lo: int, pi: int, hi: int) -> int:
    """
    requires 0 <= lo and lo <= pi and pi < hi and hi <= len(A)
    ensures lo <= result and result < hi
    ensures geSeg(A[result], A, lo, result)
    ensures leSeg(A[result], A, result, hi)
    """
    pivot = A[pi]
    swap(A, lo, pi)

    left = lo + 1
    right = hi

    while (left<right):
        assert lo+1 <= left and left <= right and right <= hi
        assert geSeg(pivot, A, lo+1, left)
        assert leSeg(pivot, A, right, hi)
        if (A[left] <= pivot):
            left += 1
        else:
            assert A[left] > pivot
            swap(A, left, right-1)
            right -= 1
    
    swap(A, lo, left-1)
    return left-1


# Quick Sort
# Best & Average: O(nlogn) Worst: O(n^2)
def quickSort(A: Iterable[int], lo: int, hi: int) -> None:
    """
    Implementation of Quick Sort
    requires 0 <= lo and lo <= hi and hi <= len(A)
    ensures isSorted(A, lo, hi)
    """
    if (hi-lo <= 1): return
    pi = random.randint(lo, hi-1) #random index of the array

    mid = partition(A, lo, pi, hi)
    quickSort(A, lo, mid)
    quickSort(A, mid+1, hi)
    return

A = [1,5,6,7,3,4]
print(A)
quickSort(A, 0, len(A))
print(A)

def merge(A: Iterable[int], lo: int, mid: int, hi: int) -> None:
    """
    requires 0 <= lo and lo <= mid and mid <= hi and hi <= len(A)
    requires isSorted(A, lo, mid) and isSorted(A, mid, hi)
    ensures isSorted(A, lo, hi)
    """
    B = [0] * len(A)
    i, j, k = lo, mid, 0

    # Compare i and j, put the lower element into the sorted array
    while (i < mid and j < hi):
        assert lo <= i and i <= mid
        assert mid <= j and j <= hi
        assert k == (i - lo) + (j - mid)
        if (A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            assert A[i] > A[j]
            B[k] = A[j]
            j += 1
        k += 1
    
    assert i == mid or j == hi
    # Put any remaining elements into the sorted array
    while (i < mid):
        B[k] = A[i]
        i += 1
        k += 1
    while (j < hi):
        B[k] = A[j]
        j += 1
        k += 1
    
    # Put back the sorted array into the original array
    for i in range(hi-lo):
        A[lo+i] = B[i]
        

# Merge Sort
# O(nlogn)
def mergeSort(A: Iterable[int], lo: int, hi: int) -> None:
    """
    Implementation of Merge Sort
    requires 0 <= lo and lo <= hi and hi <= len(A)
    ensures isSorted(A, lo, hi)
    """
    if (hi-lo <= 1): return
    mid = lo + (hi-lo)//2

    mergeSort(A, lo, mid)
    mergeSort(A, mid, hi)
    merge(A, lo, mid, hi)
    return

A = [1,5,6,7,3,4]
print(A)
mergeSort(A, 0, len(A))
print(A)