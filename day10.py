import doctest
import common
import logging
from collections import defaultdict
import re
import matplotlib.pyplot as plt
import numpy
import math

logging.basicConfig(level=logging.DEBUG)

day = 10


def main():
    # exampledata, data = common.opendata()
    datafile = f"./day{day}_input.txt"
    data = open(datafile, 'r').readlines()

    print(part1(data))
    #print(part2(data))


def part1(inputdata):
    """

    :param inputdata:
    :return:
    """
    sparsemap = {} # Map ID of point (an int) to (x, y, xvel, yvel)


    pattern = r"position=<((?: |-)*\d*),((?: |-)*\d*)> velocity=<((?: |-)*\d*),((?: |-)*\d*)>"

    for i, line in enumerate(inputdata):
        m = re.search(pattern, line)
        sparsemap[i] = list(map(int, m.groups()))  # x, y, xvel, yvel


    for i in range(1000000):
        x_point1 = sparsemap[0][0]
        updates_before_plot = math.ceil(abs(x_point1)/10)
        if 300 > abs(x_point1):
            updates_before_plot = 5
        if  115 < x_point1 < 150:
            updates_before_plot = 1
            if i % updates_before_plot == 0:
                plot_map(sparsemap)
                print(f"sparsemap[0]: {sparsemap[0]}")

        sparsemap = update_position(sparsemap)

def plot_map(sparsemap):
    x = []
    y = []
    for el in sparsemap.values():
        x.append(el[0])
        y.append(el[1])


    plt.scatter(x, y)
    plt.show()


def update_position(sparsemap):
    # Key: x, y, xvel, yvel
    for key in sparsemap:
        x, y, xvel, yvel = sparsemap[key]
        sparsemap[key] = (x + xvel), y + yvel, xvel, yvel
    return sparsemap



if __name__ == '__main__':
    main()