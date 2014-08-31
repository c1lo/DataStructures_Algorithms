__author__ = 'xiyilo'


class Array(object):
    """
    extending Python lists - an array class
    """
    def __init__(self, length=0, baseIndex=0):
        assert length >= 0
        self._data = [None for i in xrange(length)]
        self._baseIndex = baseIndex

    def __copy__(self):
        result = Array(len(self._data))
        for i, datum in enumerate(self._data):
            result._data[i] = datum
        result._baseIndex = self._baseIndex
        return result

    def getOffset(self, index):
        offset = index - self._baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return  offset

    def __getitem__(self, item):
        return self._data[self.getOffset(item)]

    def __setitem__(self, key, value):
        self._data[self.getOffset(key)] = value

    # Array Properties
    def getData(self):
        return self._data

    data = property(
        fget=lambda self: self.getData()
    )

    def getBaseIndex(self):
        return self._baseIndex

    def setBaseIndex(self, baseIndex):
        self._baseIndex = baseIndex

    baseIndex = property(
        fget=lambda self: self.getBaseIndex(),
        fset=lambda self, value: self.setBaseIndex(value)
    )

    # Resizing an array
    def __len__(self):
        return len(self._data)

    def setLength(self, value):
        if len(self._data) != value:
            newData = [None for i in xrange(value)]
            m = min(len(self._data), value)
            for i in xrange(m):
                newData[i] = self._data[i]
            self._data = newData

    length = property(
        fget=lambda self: self.__len__(),
        fset=lambda self, value: self.setLength(value)
    )




if __name__=='__main__':
    from copy import copy

    a = Array(5)
    b = copy(a)

    print a
    print a[0]
    print id(a)
    print(b)
    print id(b)