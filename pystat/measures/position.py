import functools


def average(sample: list) -> float:
    sum = functools.reduce(lambda previous, actual: previous + actual, sample)
    return sum / len(sample)


def median(sample: list) -> float:
    sample.sort()
    index = len(sample) // 2
    if (len(sample) % 2) == 0:
        return average([sample[index - 1], sample[index]])

    return sample[index]


def mode(sample: list):
    max_element = max(sample) + 1
    frequency_table = max_element * [0]
    for i in sample:
        frequency_table[i] += 1
    modes = list()
    qtd_frequency = frequency_table[0]
    for i in range(0, len(frequency_table)):
        if (frequency_table[i] > qtd_frequency):
            qtd_frequency = frequency_table[i]
            modes.clear()
            modes.append(i)
        elif (frequency_table[i] == qtd_frequency):
            modes.append(i)

    return modes


if __name__ == '__main__':
    print(mode([1, 1, 2, 2, 3, 4, 7, 9, 9, 0, 3]))
