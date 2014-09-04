__author__ = 'xiyilo'


class Visitor(object):
    """
    Visitor interfaceAn visitor provides the means to access
    one-by-one all the objects in a container and to perform
    a given operation on those objects.
    """
    def __init__(self):
        super(Visitor, self).__init__()

    def visit(self, obj):
        pass

    def getIsDone(self):
        return False

    isDone = property(
        fget=lambda self: self.getIsDone()
    )


class PrintingVisitor(Visitor):
    def visit(self, obj):
        print obj


class MatchingVisitor(Visitor):
    def __init__(self, target):
        self.target = target
        self.found = None

    def visit(self, obj):
        if not self.isDone and obj == self.target:
            self.found = obj

    def isDone(self):
        return self.found is not None