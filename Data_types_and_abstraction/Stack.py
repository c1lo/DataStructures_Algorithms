__author__ = 'xiyilo'


import sys
sys.path.append('/home/xiyilo/PycharmProjects/DataStructures&Algorithms/Foundational_data_structures')


import Foundational_data_structures.Array as Array
from abc import abstractmethod
from Container import Container, Iterator
import Visitor


class Stack(Container):
    """
    Abstract Stack class
    """
    def __init__(self):
        super(Stack, self).__init__()

    def getTop(self):
        pass
    getTop = abstractmethod(getTop)
    top = property(
        fget=lambda self: self.getTop()
    )

    def push(self, obj):
        pass
    push = abstractmethod(push)

    def pop(self):
        pass
    pop = abstractmethod(pop)


class StackAsArray(Stack):
    def __init__(self, size=0):
        super(StackAsArray, self).__init__()
        self._array = Array.Array(size)

    def purge(self):
        while self._count > 0:
            self._array[self._count] = None
            self._count -= 1

    def push(self, obj):
        if self._count == len(self._array):
            raise ContainerFull
        self._array[self._count] = obj
        self._count += 1

    def pop(self):
        if self._count == 0:
            raise ContainerEmpty
        self._count -= 1
        result = self._array[self._count]
        self._array[self._count] = None
        return result

    def getTop(self):
        if self._count == 0:
            raise ContainerEmpty
        return self._array[self._count - 1]

    def accept(self, visitor):
        assert isinstance(visitor, Visitor)
        for i in xrange(self._count):
            visitor.visit(self._array[i])
            if visitor.isDone:
                return

    class Iterator(Iterator):
        def __init__(self, stack):
            super(StackAsArray.Iterator, self).__init__(stack)
            self._position = 0

        def next(self):
            if self._position >= self._container._count:
                raise StopIteration
            obj = self._container._array[self._position]
            self._position += 1
            return obj

    def __iter__(self):
        return self.Iterator(self)










if __name__ == '__main__':
    """
    Fail to implement this main routine......
    """
    stack = StackAsArray(57)
    stack.push(3)
    stack.push(2)
    stack.push(4)

    for obj in stack:
        print obj