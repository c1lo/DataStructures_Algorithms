__author__ = 'xiyilo'

from abc import abstractmethod
from Visitor import Visitor, MatchingVisitor

class Container(object):
    def __init__(self):
        super(Container, self).__init__()
        self._count = 0

    def purge(self):
        pass
    purge = abstractmethod(purge)

    def __iter__(self):
        pass
    __iter__ = abstractmethod(__iter__)

    def getCount(self):
        return self._count
    count = property(
        fget=lambda self: self.getCount()
    )

    def getIsEmpty(self):
        return self.count == 0
    isEmpty = property(
        fget=lambda self: self.getIsEmpty()
    )

    def getIsFull(self):
        return False
    isFull = property(
        fget=lambda self: self.getIsFull()
    )

    def accept(self, visitor):
        assert isinstance(visitor, Visitor)
        for obj in self:
            visitor.visit(obj)

    class StrVisitor(Visitor):

        def __init__(self):
            self._string = ""
            self._comma = False

        def visit(self, obj):
            if self._comma:
                self._string = self._string + ','
            self._string = self._string + str(object)
            self._comma = True

        def __str__(self):
            return self._string

    def __str__(self):
        visitor = Container.StrVisitor()
        self.accept(visitor)
        return '%s {%s}' % (self.__class__.__name__, str(visitor))




class Iterator(object):
    def __init__(self, container):
        super(object, self).__init__()
        self._container = container

    def __iter__(self):
        return self

    def next(self):
        pass
    next = abstractmethod(next)



class SomeContainer(Container):
    def accept(self, visitor):
        for i in self:
            if visitor.isDone:
                return
            visitor.visit(i)


class SearchableContainer(Container):
    def __init__(self):
        super(SearchableContainer, self).__init__()

    def __contains__(self, item):
        pass
    __contains__ = abstractmethod(__contains__)

    def insert(self, obj):
        pass
    insert = abstractmethod(insert)

    def withdraw(self, obj):
        pass
    withdraw = abstractmethod(withdraw)

    def find(self, obj):
        pass
    find = abstractmethod(find)


