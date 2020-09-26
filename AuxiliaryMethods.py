from typing import Iterable

# O(n)
def isSorted(A: Iterable[int], lo: int, hi: int) -> bool:
    """
    Returns true if the array segment A[lo..hi] is sorted
    requires 0 <= i and i < len(A)
    requires 0 <= j and j < len(A)
    """
    if (lo == hi): return True
    return leSeg(A[lo], A, lo+1, hi) and isSorted(A, lo+1, hi)

# O(n)
def geSeg(x: int, A: Iterable[int], lo: int, hi: int) -> bool:
    """
    Returns true if x >= A[lo..hi]
    """
    if (lo == hi): return True
    return (x >= A[lo] and geSeg(x, A, lo+1, hi))

# O(n)
def leSeg(x: int, A: Iterable[int], lo: int, hi: int) -> bool:
    """
    Returns true if x <= A[lo..hi]
    """
    if (lo == hi): return True
    return (x <= A[lo] and leSeg(x, A, lo+1, hi))

# O(n)
def leSegs(A: Iterable[int], lo1: int, hi1: int, B: Iterable[int], lo2: int, hi2: int) -> bool:
    """
    Returns true if A[lo1..hi1] <= A[lo2..hi2]
    """
    if (lo1 == hi1): return True
    return leSeg(A[lo1], B, lo2, hi2) and leSegs(A, lo1+1, hi1, B, lo2, hi2)

# O(1)
def swap(A: Iterable[int], i: int, j: int) -> None:
    """
    Swaps A[i] with A[j]
    """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

# O(n)
def findMin(A: Iterable[int], lo: int, hi: int) -> int:
    """
    Returns the index m of a minimal element in the non-empty segment A[lo..hi]
    requires 0 <= lo and lo < hi and hi <= len(A)
    ensures lo <= result and result < hi
    ensures leSeg(A[result], A, lo, hi)
    """
    min = lo
    for i in range(lo+1, hi):
        assert lo < i and i <= hi
        assert lo <= min and min < hi
        assert leSeg(A[min], A, lo, i)
        if (A[i] < A[min]):
            min = i
    return min