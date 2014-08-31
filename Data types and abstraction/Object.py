__author__ = 'xiyilo'

from abc import abstractmethod

class ABObject(object):
    def __init__(self):
        super(ABObject, self).__init__()

    def __cmp__(self, other):
        if isinstance(self, other.__class__):
            return self._compareTo(other)
        elif isinstance(other, self.__class__):
            return -other._compareTo(self)
        else:
            return cmp(self.__class__.__name__, other.__class__.__name__)


    def _compareTo(self, other):
        pass
    _compareTo = abstractmethod(_compareTo)


class DerivedABObject(ABObject):
    def __init__(self, Var):
        self.intVar = Var

    def _compareTo(self, other):
        return cmp(self.intVar, other.intVar)


if __name__ == '__main__':

    from socket import socket

    obj1 = DerivedABObject(1)
    obj2 = DerivedABObject(2)

    obj3 = socket()

    print 'The same classes'
    print obj1._compareTo(obj2)
    print obj1.__cmp__(obj2)
    print cmp(obj1, obj2)
    print cmp(obj2, obj1)
    print obj1 < obj2
    print obj1 == obj2


    print 'Different classes:'
    print obj1.__class__.__name__
    print obj3.__class__.__name__
    print obj1 < obj3
