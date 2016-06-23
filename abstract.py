'''
Use inheritance to refactor and avoid copy-pasting methods in a class.

Mixins
    Classes meant for inheritance only.
    Not meant to instantiate.

Mixins are GREAT!
    They provide quick and easy functionality.
    Making a new class is as easy as writing a list of capabilities.

Mixins are TERRIBLE!
    It's easy to accidentally instantiate a mixin.
    And it's easy to forget to implement required methods on a subclass.

Abstract Base Classes (ABCs) to the rescue!
    ABCs prevent an abstract class from being instantiated.
    ABCs also enforce that child classes implement required methods.
'''

from abc import ABCMeta, abstractmethod


class Capper(object):  # Py3k:  Capper(metaclass=ABCMeta)

    __metaclass__ = ABCMeta
    
    'inherit this to gain capitalize capability'
    def capitalize(self):
        return ''.join([c.upper() for c in self])

    @abstractmethod
    def __getitem__(self, index):
        return None

class Uncapper:
    'inherit this to gain lowercasing capability'
    def uncapitalize(self):
        return ''.join([c.lower() for c in self])

class SkipSeq(Capper, Uncapper):
    ''' A sequence that skips every other element.

    >>> skip = SkipSeq('abcdefg')
    >>> skip[0]
    'a'
    >>> skip[1]
    'c'
    >>> len(skip)
    4
    '''

    def __init__(self, sequence):
        self.sequence = sequence

    def __getitem__(self, index):
        return self.sequence[index * 2]

    def __len__(self):
        return (len(self.sequence) + 1) // 2


class SkipTwoSeq(Capper, Uncapper):
    ''' A sequence that keeps every 3rd element.

        >>> skip = SkipTwoSeq('abcdefg')
        >>> skip[0]
        'a'
        >>> skip[1]
        'd'
        >>> skip[2]
        'g'
        >>> len(skip)
        3
    '''

    def __init__(self, sequence):
        self.sequence = sequence

    def __getitem__(self, index):
        return self.sequence[index * 3]

    def __len__(self):
        return (len(self.sequence) + 2) // 3

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
