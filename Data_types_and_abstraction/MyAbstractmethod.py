__author__ = 'xiyilo'


import inspect

class MyAbstractmethod(object):
    """
    MyAbstractmethod class definition
    wrap a function object that is supposed to be an abstract method
    in an instance of the MyAbstractmethod class
    """
    def __init__(self, func):
        print inspect.isfunction(func)
        self._func = func

    def __get__(self, obj, type):
        return self.method(obj, self._func, type)

    class method(object):
        def __init__(self, obj, func, cls):
            self._self = obj
            self._func = func
            self._class = cls
            self.__name__ = func.__name__

        def __call__(self, *args, **kwargs):
            msg = "Abstract method %s of class %s called." % (
                self._func.__name__, self._class.__name__
            )
            print msg
            raise TypeError


if __name__ == '__main__':

    """
    we implement a __get__ method that returns an instance
    of the nested abstractmethod.method class. This class
    in turn implements a __call__ method that raises a
    TypeError exception. The effect of this is that whenever
     an abstract method is called an exception is raised.
    """

    def hello():
        print 'Hello'

    ab = MyAbstractmethod(hello)

    meth = ab.__get__(ab, object)
    meth.__call__('gg')
