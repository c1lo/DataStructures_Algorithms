__author__ = 'xiyilo'

from MultiDimensionalArray import MultiDimensionalArray

class Matrix(object):
    def __init__(self, numOfRows, numOfColumns):
        assert numOfRows >= 0
        assert numOfColumns >= 0
        super(Matrix, self).__init__()
        self._numOfRows = numOfRows
        self._numOfColumns = numOfColumns

    def getNumOfRows(self):
        return self._numOfRows

    def getNumOfColumns(self):
        return self._numOfColumns

    numOfRows = property(
        fget=lambda self: self.getNumOfRows()
    )
    numOfColumns = property(
        fget=lambda self: self.getNumOfColumns()
    )

############################################################

class DenseMatrix(Matrix):
    def __init__(self, rows, cols):
        super(DenseMatrix, self).__init__(rows, cols)
        self._array = MultiDimensionalArray(rows, cols)

    def __getitem__(self, (i, j)):
        return self._array[i, j]

    def __setitem__(self, (i, j), value):
        self._array[i, j] = value

    def __mul__(self, other):
        assert self.numOfColumns == other.numOfRows
        result = DenseMatrix(
            self.numOfRows, other.numOfColumns
        )
        for i in xrange(self.numOfRows):
            for j in xrange(other.numOfColumns):
                sumM = 0
                for k in xrange(self.numOfColumns):
                    sumM += self[i, k] * other[k, j]
                result[i, j] = sumM
        return result






if __name__ == '__main__':
    m = Matrix(2, 3)
    print m.numOfRows
    print m.numOfColumns

    m = DenseMatrix(2, 3)
    n = DenseMatrix(3, 4)

    for i in xrange(2):
        for j in xrange(3):
            m[i, j] = i + j
            print m[i, j],
        print
    print

    for i in xrange(3):
        for j in xrange(4):
            n[i, j] = i + j
            print n[i, j],
        print
    print

    m = m * n

    for i in xrange(2):
        for j in xrange(4):
            print m[i, j],
        print