#!/usr/bin/env python

import itertools

class List(list):

    # map, reduce, filter

    def map(self, function):
        return List(map(function, self))

    def reduce(self, function, initializer=None):
        return reduce(function, self, initializer)

    def filter(self, function=None):
        return List(filter(function, self))

    # list operations

    def sort(self, function=None, key=None, reverse=False):
        return List(sorted(self, function, key, reverse))

    def reverse(self):
        return List(reversed(self))

    def flatten(self):
        return List(itertools.chain.from_iterable(self))

    # info of the list: all, any

    def all(self):
        return all(self)

    def any(self):
        return any(self)

    def length(self):
        return len(self)

    # integer operations

    def max(self):
        return max(self)

    def min(self):
        return min(self)

    def sum(self):
        return sum(self)

    def average(self):
        return sum(self) * 1.0 / len(self)

    # string operations

    def join(self, separator):
        return separator.join(self)

    # component selection

    def select(self, attribute_name):
        return self.map(lambda element: element.attribute_name)

    def select_index(self, index):
        return self.map(lambda element: element[index])

    def select_key(self, key):
        return self.map(lambda element: element[key])


