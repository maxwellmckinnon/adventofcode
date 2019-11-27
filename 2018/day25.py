import doctest
import common
import logging
from collections import defaultdict
import re
import matplotlib.pyplot as plt
import numpy
import math
import random

logging.basicConfig(level=logging.DEBUG)

day = 25

exampleinput = """0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0"""

exampleinput2 = """-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0"""



def main():
    # exampledata, data = common.opendata()
    datafile = f"./day{day}_input.txt"
    data = open(datafile, 'r').read()

    print(part1(data))
    # print(part2(data))


def part1(inputdata, M=3):
    """
    Find the number of constellations given a manhattan distance M (default 3)
    :param inputdata:
    :return:

    >>> part1(exampleinput)
    2

    >>> part1(exampleinput2)
    4
    """
    constellations = []  # list of sets of 4D tuples
    currentconstellation = set()
    for line in inputdata.split('\n'):
        position = (x,y,z,t) = tuple(map(int, line.strip().split(',')))

        matchingconstellations = []  # list of set of the constellations this position is in
        # Compare against all current constellations
        for constellation in constellations:
            for position2 in constellation:
                if manhatdist(position, position2) <= M:
                    matchingconstellations.append(constellation)
                    break


        # combine position with constellation it matches with and combine constellations if they all connect via it
        if len(matchingconstellations) == 0:
            constellation = set()
            constellation.add(position)
            constellations.append(constellation)
        # elif len(matchingconstellations) == 1:
        #     matchingconstellations[0].add(position)
        elif len(matchingconstellations) >= 1:
            combined_constellation = set()
            combined_constellation.add(position)
            for constellation in matchingconstellations:
                constellations.remove(constellation)
                combined_constellation = combined_constellation.union(constellation)
            constellations.append(combined_constellation)

    logging.debug(constellations)
    return(len(constellations))



def manhatdist(a, b):
    """
    Given tuple a(x1, y1, z1, t1) and b, compute manhattan distance

    :param a:
    :param b:
    :return:

    >>> manhatdist((1,2,3),(0,-1,0))
    7

    """

    s = 0
    for i,j in zip(a,b):
        s += abs(i-j)
    return s



if __name__ == '__main__':
    main()