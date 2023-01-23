"""
Core module of 'constancy'.

"""
from collections import OrderedDict
from copy import deepcopy


class Constants(object):
    """Immutable container of constant."""

    __slots__ = "__dict__"

    def __init__(self, **kwargs):

        if list(filter(lambda x: not x.isupper(), kwargs)):
            raise AttributeError("Name of constant should be uppercase.")

        super(Constants, self).__setattr__(
            "__dict__", OrderedDict(map(lambda x: (x[0], deepcopy(x[1])), kwargs.items()))
        )

    def sort(self, key=None, reverse=False):
        """
        >>> DAYS.sort(lambda x: x[1], True); list(DAYS)
        ['SUN', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON']
        """

        super(Constants, self).__setattr__(
            "__dict__",
            OrderedDict(sorted(self.__dict__.items(), key=key, reverse=reverse)),
        )

    def __getitem__(self, name):
        """
        >>> DAYS['MON']
        1
        """
        return self.__dict__[name]

    def __len__(self):
        """
        >>> len(DAYS)
        7
        """
        return len(self.__dict__)

    def __iter__(self):
        for name in self.__dict__:
            yield name

    def keys(self):
        """Return list of attributes. Allow to 'dict' conversion."""
        return list(self)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, str(self.__dict__))

    def __dir__(self):
        return list(self)

    def __setattr__(self, key, value):
        """
        >>> DAYS.MON = 0
        Traceback (most recent call last):
        ...
        AttributeError: Immutable attribute
        """
        raise AttributeError("Immutable attribute")

    def __delattr__(self, key):
        """
        >>> del DAYS.MON
        Traceback (most recent call last):
        ...
        AttributeError: Immutable attribute
        """
        raise AttributeError("Immutable attribute")

    def __getattr__(self, key):
        """Enable an autocomplete.
        >>> DAYS.MON
        1
        """
        return self.__dict__[key]


if __name__ == "__main__":
    DAYS = Constants(MON=1, TUE=2, WED=3, THU=4, FRI=5, SAT=6, SUN=7)
    import doctest

    doctest.testmod(extraglobs=DAYS)
