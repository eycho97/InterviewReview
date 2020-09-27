from typing import Iterable
import Node
    
class Stack:

    @staticmethod
    def isStack(self, S: 'Node') -> bool:
        return NotImplementedError

    def stackEmpty(self) -> bool:
        """
        requires S != None
        """
        raise NotImplementedError

    def peek(self) -> str:
        """
        requires not stackEmpty()
        """
        raise NotImplementedError

    def stackSize(self) -> int:
        """
        ensures result >= 0
        """
        raise NotImplementedError

    def pop(self) -> str:
        """
        requires not stackEmpty()
        """
        raise NotImplementedError

    def push(self, x: str) -> None:
        """
        ensures not stackEmpty()
        """
        raise NotImplementedError

    def stackPrint(self) -> None:
        raise NotImplementedError
    

class StackL(Stack):
    """
    Stack Class implemented with a linked list of nodes
    """
    def __init__(self, top: 'Node'=None, floor: 'Node'=None):
        self.top = top
        self.floor = floor
    
    # O(n)
    @staticmethod
    def isStack(self, S: 'Node') -> bool:
        return S.top != None and S.floor != None and Node.isSegmentSlit(S.top, S.floor)

    # O(1)
    def stackEmpty(self) -> bool:
        """
        requires S != None
        """
        return self.top == self.floor


    # O(1)
    def peek(self) -> str:
        """
        requires S != None and not stackEmpty(S)
        """
        x = self.pop()
        self.push(x)
        return x
    
    # O(n)
    def stackSize(self) -> int:
        """
        requires S != None
        ensures result >= 0
        """
        count = 0
        T = StackT.stacknew()
    
        while (not stackEmpty(S)):
            push(T, pop(S))
            count += 1
        while (not stackEmpty(T)):
            push(S, pop(T))
        return count
    
    # O(1)
    def pop(self) -> str:
        """
        requires Stack.isStack(self) not stackEmpty()
        ensures Stack.isStack(self)
        """
        e = self.top.getData()
        self.top.setNext(self.top.getNext())
        return e

    # O(1)
    def push(self, x: str) -> None:
        """
        requires Stack.isStack(self)
        ensures Stack.isStack(self) and not stackEmpty()
        """
        node = Node(x, self.top)
        self.top = node
        if (self.floor == None): self.floor = node
    
    # O(n)
    def stackPrint(self) -> None:
        """
        requires Stack.isStack(self)
        """
        original = self.top
        print("TOP: ")
        while (self.top != None):
            print(self.top.getData())
            if (self.top.getNext() != None): print(" | ")
            self.top = self.top.getNext()
        self.top = original

