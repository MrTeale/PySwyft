""" Decorators """

def endpoint(url, method="GET", expected_status=200):
    """
    Decorator for endpoints.
    """
    def dec(obj):
        obj.ENDPOINT = url
        obj.METHOD = method
        obj.EXPECTED_STATUS = expected_status
        return obj
    
    return dec


def abstractclass(cls):
    """abstractclass - class decorator

    Ensures that the class is abstract and cannot be used directly.
    """
    setattr(cls, "_ISNEVER", cls.__bases__[0].__name__)
    origInit = cls.__dict__["__init__"]

    def wrapInit(self, *args, **kwargs):
        # When a class if instantiated we can check for bases
        # we don't want it to be the base class
        try:
            assert self.__class__.__bases__[-1].__name__ != cls._ISNEVER
            origInit(self, *args, **kwargs)
        except AssertionError:
            raise TypeError("Abstract classes cannot be instantiated directly")
    
    # replace the original __init__ with the wrapped one
    setattr(wrapInit, "__doc__", getattr(origInit, "__doc__"))
    setattr(origInit, "__doc__", "")
    setattr(cls, "__init__", wrapInit)

    return cls


def extendargs(object):
    """extendargs - class decorator

    Add extra arguments to the argumentlist of the constructor of the class
    """

    def __init__(self, *loa):
        self.loa = loa
        self
    
    def __call__(self, cls):
        # save parent class __init__
        origInit = cls.__bases__[0].__dict__["__init__"]

        def wrapInit(wself, *args, **kwargs):
            for extraArg in self.loa:
                if extraArg in kwargs:
                    setattr(wself, extraArg, kwargs[extraArg])
                    del kwargs[extraArg]
            origInit(wself, *args, **kwargs)
        setattr(cls, "__init__", wrapInit)

        return cls