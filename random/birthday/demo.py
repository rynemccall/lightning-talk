#!/usr/bin/env python

""" Empirically simulate the birthday paradox

The birthday paradox is the surprisingly high change that two
people in a group of people share the same birthday.

See https://en.wikipedia.org/wiki/Birthday_problem for details.

"""

import random

from matplotlib import pyplot as plt
import numpy as np


NUMBER_OF_SIMULATIONS = 100000


def simulate_number_of_people_in_room_before_collision():
    """

    :return: Number of people added to room to achieve first collision
    :rtype: int

    """

    unique_birthdays = set()
    all_birthdays = []

    while True:
        birthday_ordinal = random.randint(0, 365 - 1)

        unique_birthdays.add(birthday_ordinal)
        all_birthdays.append(birthday_ordinal)

        if len(unique_birthdays) != len(all_birthdays):
            return len(all_birthdays)


def generate_histogram(s):
    plt.hist(
        s,
        bins=xrange(max(s)),
        color='green',
    )

    plt.ylabel('Number of simulations')
    plt.xlabel('Number of people in room when first birthday collision occurs')

    plt.axvline(
        sum(s) / NUMBER_OF_SIMULATIONS,
        color='red',
        linewidth=2,
        linestyle='--'
    )

    plt.show()


def generate_cdf(s):
    normed_counts, bin_edges = np.histogram(s, bins=max(s), normed=True)
    cdf = np.cumsum(normed_counts)

    plt.plot(
        bin_edges[1:],
        cdf,
        linewidth=2,
    )

    plt.ylabel('CDF')
    plt.xlabel('Number of people in room when first birthday collision occurs')

    plt.axhline(
        .5,
        color='red',
        linewidth=2,
        linestyle='--'
    )

    plt.show()


simulations = [
    simulate_number_of_people_in_room_before_collision()
    for _ in xrange(0, NUMBER_OF_SIMULATIONS)
]

generate_histogram(simulations)
generate_cdf(simulations)
