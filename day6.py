import sys
import doctest
import common
import logging
import numpy as np
from copy import deepcopy
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
day = 6


def main():
    # exampledata, data = common.opendata()
    datafile = f"./day{day}_input.txt"
    data = open(datafile, 'r').readlines()

    print(part1(data))
    print(part2(data))


def part1(inputdata: str):
    """

    :param inputdata:
    :return:

    Example:
    >>> part1(part1_example_data())
    17
    """
    G = Grid(inputdata)
    print(G)
    print(G.sparsegrid)

    # Find the finite areas and add their principal locations to a sparse grid
    # Find which ones extend to infinity by doing a check around the existing border frame
    boundary_labels = G.get_boundary_labels()
    print(boundary_labels)
    finitesparse = set(G.sparsegrid.values()) - boundary_labels
    # For those remaining, fill in and count based on nearest manhattan neighbor (use negatives for the filled in pieces)
    finitecounts = defaultdict(lambda:0)  # mapping of id to times it occurs
    for i in range(G.maxrows+1):
        for j in range(G.maxcols + 1):
            label, distance_to_label = G.nearest_ID_manhat_distance(i, j)
            if label in finitesparse:
                finitecounts[label]+=1

    print(finitecounts)
    maxkey = max(finitecounts, key=lambda k:finitecounts[k])
    print(f"maxkey: {maxkey}")
    print(f"value: {finitecounts[maxkey]}")
    return finitecounts[maxkey]


def part2(inputdata):
    """
    Find all squares with a total to all regions of less than 10000

    Brute force although there's a good search way to do this too...
    :param inputdata:
    :return:
    """
    magic_distance = 10000
    count = 0
    G = Grid(inputdata)
    G_visualizer = deepcopy(G)

    for i in range(G.maxrows + 1):
        for j in range(G.maxcols + 1):
            distance = 0
            for (r, c), id in G.sparsegrid.items():
                distance += abs(r - i) + abs(c - j)
            if distance < magic_distance:
                print("Magic Found")
                G_visualizer.grid[i, j] = 22.22
                count += 1

    print(G_visualizer)
    return count

class Grid:
    """Note: uses positive numbers to represent original locations and negative to represent the solved manhattan distance"""
    def __init__(self, data):
        self.sparsegrid = {}  # mapping of tuples to value
        self.maxcols = int(max(data, key=lambda x: int((x.split(',')[0].strip())) ).split(',')[0].strip() )
        self.maxrows = int(max(data, key=lambda x: int((x.split(',')[1].strip())) ).split(',')[1].strip() )
        self.grid = np.zeros([self.maxrows+1, self.maxcols+1])
        counter = 1
        for line in data:
            col, row = int(line.split(',')[0].strip()), int(line.split(',')[1].strip())
            self.grid[row][col] = counter
            self.sparsegrid[(row, col)] = counter
            counter += 1

    def __str__(self):
        return str(self.grid)

    def nearest_ID_manhat_distance(self, row, col):
        """Given a row and col, find the closest match
        Brute force, check all the sparse entries
        If two best answers occur, then return 0

        return (id, distance)
        """

        leastdistance = sys.maxsize
        leastdistanceid = 0
        double = False

        for (r, c), id in self.sparsegrid.items():
            distance = abs(row - r) + abs(col - c)
            if distance < leastdistance:
                leastdistance = distance
                leastdistanceid = id
                double = False
            elif distance == leastdistance:
                double = True

        return (0, leastdistance) if double else (leastdistanceid, leastdistance)

    def get_boundary_labels(self):
        """Return a set of the only labels found surrounding the grid"""
        boundary_labels = set()

        # Sweep the two columns
        for i in range(-1, self.maxrows + 2):
            for j in [-1, self.maxcols + 1]:
                boundary_label, distance_to_label = self.nearest_ID_manhat_distance(i, j)
                boundary_labels.add(boundary_label)

        # Sweep the two rows
        for i in [-1, self.maxrows + 2]:
            for j in range(-1, self.maxcols + 1):
                boundary_label, distance_to_label = self.nearest_ID_manhat_distance(i, j)
                boundary_labels.add(boundary_label)

        return boundary_labels


def part1_example_data():
    datafile = f"./day{day}_exampleinput.txt"
    data = open(datafile, 'r').readlines()
    return data


if __name__ == '__main__':
    main()