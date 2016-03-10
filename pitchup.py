from itertools import combinations, chain

__author__ = 'josebermudez'


# Write a program to find a pitch based on this clue: Join us at pitch x. x is a number between 1 and
# 553 such that the sum of x's divisors (not including x) is greater than x but no subset of x's divisors
# add up to exactly x


def calculate_divisors(num):
    """
    Get the divisors from a num
    :param num: number
    :return: set of divisors
    """
    return set(reduce(list.__add__, ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0)))


def calculate_sum(nums):
    """
    Get sum of a list, 0 if the list is empty.
    :param nums: list
    :return: sum
    """
    return sum(nums) if len(nums) > 0 else 0


def check_subsets(divisors, num):
    """
    Check subsets and compare the sum with number, return True if
    :param divisors: divisors of a number
    :param num: number
    :return: boolean
    """
    # check all combinations
    for comb in chain(*map(lambda x: combinations(divisors, x), range(1, len(divisors)))):
        if sum(comb) == num:
            return False

    return True


# loop from 1 to 553
for x in xrange(1, 554):
    # divisor of x, excluding x
    divisors = list(calculate_divisors(x))
    divisors.remove(x)

    # check conditions
    if calculate_sum(divisors) > x and check_subsets(divisors, x):
        print 'Pitch finded:', x
