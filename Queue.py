from typing import Iterable
from Node import Node

class Queue:
    """
    Queue Interface
    """
    @staticmethod
    def isQueue(Q: 'Node') -> bool:
        return NotImplementedError

    def queueEmpty(self) -> bool:
        """
        requires self != None
        """
        return NotImplementedError
    
    def enq(self, e: str) -> None:
        """
        requires self != None
        ensures !self.queueEmpty()
        """
        return NotImplementedError

    def deq(self) -> str:
        """
        requires self != None
        requires !self.queueEmpty()
        """
        return NotImplementedError

    def queuePrint(self) -> None:
        """
        requires self != None
        """
        return NotImplementedError
    
class QueueL:
    """
    Queue implementation with a linked list
    """

    def __init__(self, front: 'Node' = Node()):
        self.front = front
        self.back = front
    
    # O(n)
    @staticmethod
    def isQueue(Q: 'Queue'):
        return Q.front != None and Q.back != None and Node.isSegmentSlit(Q.front, Q.back)
    
    # O(1)
    def queueEmpty(self):
        """
        requires self != None
        """
        return self.front == self.back

    # O(1)
    def enq(self, s: str) -> None:
        """
        requires isQueue(self)
        ensures isQueue(self) and !self.queueEmpty()
        """
        node = Node()
        self.back.setData(s)
        self.back.setNext(node)
        self.back = node
    
    # O(1)
    def deq(self) -> str:
        """
        requires isQueue(self)
        requires !self.queueEmpty()
        """
        s = self.front.getData()
        self.front = self.front.getNext()
        return s
    
    # O(n)
    def queuePrint(self) -> None:
        """
        requires isQueue(self)
        """
        pointer = self.front
        print("Front: ", end =" ")
        while (pointer != self.back):
            print(pointer.getData(), end=" ")
            if (pointer.getNext() != self.back):
                print("<<", end =" ")
            pointer = pointer.getNext()
        print(" :Back")


