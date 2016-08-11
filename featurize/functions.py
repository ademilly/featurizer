import numpy as np


def the_sum(x):

    return sum(x)


def the_average(x):

    return np.mean(x)


def the_median(x):

    return np.median(x)


def the_min(x):

    return min(x)


def the_max(x):

    return max(x)

def the_norm(x):

    return np.array(x).dot(np.array(x))
