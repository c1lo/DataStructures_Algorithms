__author__ = 'xiyilo'


class Association(object):
    def __init__(self, *args):
        if len(args) == 1:
            self._tuple = (args[0], None)
        elif len(args) == 2:
            self._tuple = args
        else:
            raise ValueError

    def getKey(self):
        return self._tuple[0]
    key = property(
        fget=lambda self: self.getKey()
    )

    def getValue(self):
        return self._tuple[1]
    value = property(
        fget=lambda self: self.getValue()
    )

    def __cmp__(self, other):
        assert isinstance(self, other.__class__)
        return cmp(self.key, other.key)

    def __str__(self):
        return 'Association %s' % str(self._tuple)


if __name__ == '__main__':
    a = Association(3)
    print a
    b = Association(2, 4)
    print b
    print a < b