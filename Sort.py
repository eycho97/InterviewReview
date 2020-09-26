from typing import Iterable
"""
Lecture 5 Sorting
"""

#O(n)
def isSorted(A: Iterable[int], lo: int, hi: int) -> bool:
    """
    Returns true if the array segment A[lo..hi] is sorted
    requires 0 <= i and i < len(A)
    requires 0 <= j and j < len(A)
    """
    if (lo == hi): return True
    return lessThanSeg(A[lo], A, lo+1, hi) and isSorted(A, lo+1, hi)
    
#O(n)
def lessThanSeg(x: int, A: Iterable[int], lo: int, hi: int) -> bool:
    """
    Returns true if x <= A[lo..hi]
    """
    if (lo == hi): return True
    return (x <= A[lo] and lessThanSeg(x, A, lo+1, hi))

#O(n)
def lessThanSegs(A: Iterable[int], lo1: int, hi1: int, B: Iterable[int], lo2: int, hi2: int) -> bool:
    """
    Returns true if A[lo1..hi1] <= A[lo2..hi2]
    """
    if (lo1 == hi1): return True
    return lessThanSeg(A[lo1], B, lo2, hi2) and lessThanSegs(A, lo1+1, hi1, B, lo2, hi2)

#O(1)
def swap(A: Iterable[int], i: int, j: int) -> None:
    """
    Swaps A[i] with A[j]
    """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

#O(n)
def findMin(A: Iterable[int], lo: int, hi: int) -> int:
    """
    Returns the index m of a minimal element in the non-empty segment A[lo..hi]
    requires 0 <= lo and lo < hi and hi <= len(A)
    ensures lo <= result and result < hi
    ensures lessThanSeg(A[result], A, lo, hi)
    """
    min = lo
    for i in range(lo+1, hi):
        assert lo < i and i <= hi
        assert lo <= min and min < hi
        assert lessThanSeg(A[min], A, lo, i)
        if (A[i] < A[min]):
            min = i
    return min

#O(n^2)
def selectionSort(A: Iterable[int], lo: int, hi: int) -> None:
    """
    Implementation of selection sort
    requires 0 <= lo and lo <= hi and hi <= len(A)
    ensures isSorted(A, lo, hi)
    """
    for i in range(hi):
        assert lo <= i and i <= hi
        assert isSorted(A, lo, i)
        assert lessThanSegs(A, lo, i, A, i, hi)
        min = findMin(A, i, hi)
        swap(A, i, min)


# A = [1,5,6,7,3,4]
# print(A)
# selectionSort(A, 0, len(A))
# print(A)
