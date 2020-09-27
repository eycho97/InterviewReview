from typing import Iterable

class Node:
    def __init__(self, data: str, next: 'Node'=None):
        self.data = data
        self.next = next
    
    # O(1)
    def getNext(self) -> 'Node':
        return self.next

    # O(1)
    def getData(self) -> str:
        return self.data

    # O(1)
    def setNext(self, next: 'Node') -> None:
        self.next = next

    # O(1)
    def setData(self, data: str) -> None:
        self.data = data
    
    # O(n)
    @staticmethod
    def isSegmentSlit(start: 'Node', end: 'Node'):
        if (start == None): return False
        if (start == end): return True
        return isSegmentSlit(start.getNext(), end)