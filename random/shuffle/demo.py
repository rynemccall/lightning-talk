#!/usr/bin/env python

import copy
import random

NUMBER_OF_SIMULATIONS = 100000


def shuffle(items):
    """ A biased implementation of the Fisher-Yates shuffle

    :return: List[items]
    :rtype: List[Any]

    """

    items = copy.deepcopy(items)

    for i, _ in enumerate(items):
        swap_index = random.randint(0, len(items) - 1)
        temp = items[swap_index]

        items[swap_index] = items[i]
        items[i] = temp

    return items

items = ['a', 'b', 'c']

shuffles = [
    shuffle(items)
    for _ in xrange(0, NUMBER_OF_SIMULATIONS)
]

for item in items:
    for i in xrange(0, len(items)):
        print "Number of times {} is in position {}: {}".format(
            item,
            i,
            len([
                x for x in shuffles
                if x[i] == item
            ])
        )

    print ''
