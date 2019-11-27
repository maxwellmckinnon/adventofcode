
import doctest
import common
import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)

children = {}
meta = defaultdict(lambda: [])
id_count = 0  # give each new node seen a new ID


def main():
    exampledata, data = common.opendata()

    print(part1(data))


def part1(inputdata: list):
    """

    :param inputdata:
    :return:

    Example:
    >>> part1("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    138

    """
    # global id_count
    # global children
    # global meta

    if type(inputdata) != list:
        inputdata = inputdata.split()
    if len(inputdata) == 0:
        return

    id = id_count
    id_count += 1
    quantitychildren = inputdata.pop(0)
    if quantitychildren == 0:  # No children
        quantitymeta = inputdata.pop(0)
        for m in range(quantitymeta):
            meta[id].append(m)
    elif quantitychildren > 0:











if __name__ == '__main__':
    main()