# python-functional-list

A list subclass wraps functions, providing syntax sugar for functional programming

## Motivation

Python has much support for basic functional programming.
However, when multiple functions are applied at the same time,
it is not easy to read, for example:

    l = [1, 2, 3, 4, 5]
    sum(filter(None, map(lambda x: x-4, map(lambda x: x**2, l))))
    sum([ x**2 - 4 for x in l if x**2 - 4])

This module provides a subclass of `list` with frequently used function as methods.
A jQuery-like statement can be written.

## Notes

* For `map`, `filter`, and anything based on them, the result is also an instance of this class.
  Therefore you can call another function on this result.

* For `min`, `max`, `length`, and anything alike, the result is an integer.

* `sum` and `reduce` requires the add operator; `average` further requires the divide operator.
  In most cases, they are used with lists of numbers.

* `join` is used with strings.

## Usage

    from functional_list import List

    l = List([1,2,3,4,5])
    l.sum()
    l.map(lambda x: x**2).map(lambda x: x-4).filter().sum()

    l = List([{'a': 1}, {'a': 2}])
    l.select_key('a').average()

    l = List(['line 1', 'line 2', 'line 3'])
    l.join('\n')

