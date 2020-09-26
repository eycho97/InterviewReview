from typing import Iterable
"""
Lecture 4 Search
"""

# O(n)
def isIn(x: int, A: Iterable[int], lo: int, hi: int) -> bool:
    # requires 0 <= lo && lo <= hi && hi <= len(A)
    for i in range(lo, hi):
        assert lo <= i and i <= hi
        if (A[i] == x): return True
    return False

# O(n)
def isSorted(A: Iterable[int], lo: int, hi: int) -> bool:
    # requires 0 <= lo && lo <= hi && hi <= len(A)
    for i in range(lo, hi-1):
        assert lo <= i
        if not (A[i] <= A[i+1]): return False
    return True


# Linear Search
# O(n)
def linearSearch(x: int, A: Iterable[int], n: int) -> int:
    """
    Implementation of Linear Search
    requires 0 <= n and n <= len(A)
    requires isSorted(A,0,n)
    ensures (result == None and not isIn(x,A,0,n)) or 
    ((0 <= result and result < n) and A[result] == x)
    """
    for i in range(n):
        assert 0 <= i and i <= n
        assert i == 0 or A[i-1] < x
        if (A[i] > x):
            return None 
        if (A[i] == x): 
            return i
    #originally -1, but in Python it would return the end of the list
    return None

# A = [0,2,5,6,12]
# print(linearSearch(5,A,len(A)))

# Binary Search
# O(log(n))
def binSearch(x:int, A:Iterable[int], n:int) -> int:
    """
    Implementation of Binary Search
    requires 0 <= n and n <= len(A)
    requires isSorted(A,0,n)
    ensures (None == result and not isIn(x, A, 0, n)) or
    ((0 <= result and result < n) and A[result] == x)
    """
    lo, hi = 0, n
    while (lo < hi):
        assert 0 <= lo and lo <= hi and hi <= n
        assert (lo == 0 or A[lo-1] < x)
        assert (hi == n or A[hi] > x)
        mid = lo + (hi-lo)//2
        if (A[mid] == x): 
            return mid
        if (A[mid] < x):
            low = mid + 1
        else: #A[mid] > x
            hi = mid
    return None

# print(binSearch(5,A,len(A)))