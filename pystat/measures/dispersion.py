import math

from pystat.measures.position import average


def variance(samples: list) -> float:
    average_of_sample = average(samples)
    sum_of_dif = sum(map(lambda sample: math.pow((sample - average_of_sample), 2), samples))
    return sum_of_dif / len(samples)


def standard_deviation(samples: list) -> float:
    return math.sqrt(variance(samples))
