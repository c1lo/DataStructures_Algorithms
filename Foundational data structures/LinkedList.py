__author__ = 'xiyilo'


class LinkedList(object):
    class Element(object):
        def __init__(self, list, datum, next):
            self._list = list
            self._datum = datum
            self._next = next

        def getDatum(self):
            return self._datum

        datum = property(
            fget=lambda self: self.getDatum()
        )

        def getNext(self):
            return self._next

        next = property(
            fget=lambda self: self.getNext()
        )

        def insertAfter(self, item):
            self._next = LinkedList.Element(
                self._next, item, self._next
            )
            if self._list._tail is self:
                self._list._tail = self._next

        def insertBefore(self, item):
            tmp = LinkedList.Element(self._list, item, self)
            if self is self._list._head:
                self._list._head = tmp
            else:
                prevPtr = self._list._head
                while prevPtr is not None and prevPtr._next is not self:
                    prevPtr = prevPtr._next
                prevPtr._next = tmp


    def __init__(self):
        self._head = None
        self._tail = None

    def purge(self):
        self._head = None
        self._tail = None

    def getHead(self):
        return self._head

    head = property(
        fget=lambda self: self.getHead()
    )

    def getTail(self):
        return self._tail

    tail = property(
        fget=lambda self: self.getTail()
    )

    def getIsEmpty(self):
        return self._head is None

    isEmpty = property(
        fget=lambda self: self.getIsEmpty()
    )

    def getFirst(self):
        if self._head is None:
            print 'ContainerEmpty'
            return5
        return self._head.datum

    first = property(
        fget=lambda self: self.getFirst()
    )

    def getLast(self):
        if self._tail is None:
            print 'ContainerEmpty'
            return
        return self._tail.datum

    last = property(
        fget=lambda self: self.getLast()
    )

    def prepend(self, item):
        tmp = self.Element(self, item, self._head)
        if self._head is None:
            self._tail = tmp
        self._head = tmp

    def append(self, item):
        tmp = self.Element(self, item, None)
        if self._head is None:
            self._head = tmp
        else:
            self._tail._next = tmp
        self._tail = tmp

    def __copy__(self):
        result = LinkedList()
        ptr = list._head
        while ptr is not None:
            result.append(ptr._datum)
            ptr = ptr._next
        return result

    def extract(self, item):
        ptr = self._head
        prevPtr = None
        while ptr is not None and ptr._datum is not item:
            prevPtr = ptr
            ptr = ptr._next
        if ptr is None:
            raise KeyError
        if ptr == self._head:
            self._head = ptr._next
        else:
            prevPtr._next = ptr._next
        if ptr == self._tail:
            self._tail = prevPtr

    def printAll(self):
        ptr = self._head
        while ptr is not None:
            print ptr._datum,
            ptr = ptr._next
        print


if __name__ == '__main__':
    l = LinkedList()
    print l.isEmpty

    l.last

    l.append(1)
    print l.first
    l.append(2)
    l.append(3)
    l.append(4)
    l.printAll()

    l.prepend(5)
    l.printAll()
    l.extract(3)

    l.printAll()
    print l.last

    print '###########################'

    e = LinkedList.Element(l, 1, None)
    print e._datum
    e.insertAfter(2)
    print e._next.datum
    print e
    print e._next

    l._tail.insertBefore(9)
    l.printAll()



