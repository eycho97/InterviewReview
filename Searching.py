from typing import Iterable
"""
Lecture 4 Search
"""

# O(n)
def isIn(x: int, A: Iterable[int], lo: int, hi: int): -> bool
    # requires 0 <= lo && lo <= hi && hi <= len(A)
    for i in range(lo, hi):
        #loop invariant lo <= i and i <= hi
        if (A[i] == x): return True
    return False

# O(n)
def isSorted(A: Iterable[int], lo: int, hi: int): -> bool
    # requires 0 <= lo && lo <= hi && hi <= len(A)
    for i in range(lo, hi-1):
        # loop_variant lo <= i
        if (!A[i] <= A[i+1]): return False
    return True


#Linear Search
# O(n)
def linearSearch(x: int, A: Iterable[int], n: int): -> int
    """
    requires 0 <= n and n <= len(A)
    requires isSorted(A,0,n);
    ensures (result == -1 and !isIn(x,A,0,n)) or 
    ((0 <= result and result < n) and A[result] == x)
    """
    for i in range(n):
        #loop_invariant 0 <= i and i <= n
        #loop_invariant i == 0 || A[i-1] < x
        if (A[i] > x): 
            return None 
        if (A[i] == x): 
            return i
    #originally -1, but in Python it would return the end of the list
    return None



