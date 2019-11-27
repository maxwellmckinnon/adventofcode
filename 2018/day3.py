# coding=utf-8

from collections import defaultdict
import re

datafile = "./day3_input.txt"
data = open(datafile, 'r')

landmanagement = defaultdict(lambda: set())  # map from tuple to set of claim IDs
doubledland = set()  # set of tuples
singleids = set()

def main():
    pattern = re.compile(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)")

    # Plot managed quilt land
    for line in data:
        m = re.search(pattern, line)
        id = int(m.group(1))
        leftedgeoffset = int(m.group(2))
        topedgeoffset = int(m.group(3))
        width = int(m.group(4))
        height = int(m.group(5))

        plot_land(id, leftedgeoffset, topedgeoffset, width, height)

    twoormore = 0
    for values_set in landmanagement.values():
        if len(values_set) > 1:
            twoormore += 1
    print(f"Number of plots holding two or more claims: {twoormore}")

    no_overlap_id = no_overlap_plot_id()
    print(f"This ID has no overlap: {no_overlap_id}")

    #print(landmanagement)


def plot_land(id, leftedgeoffset, topedgeoffset, width, height):
    # upper left is 0,0
    for i in range(width):
        for j in range(height):
            landmanagement[(leftedgeoffset + i, topedgeoffset + j)].add(id)


def no_overlap_plot_id():
    overlap_ids = set()  # set containing IDs which have noted overlap
    all_ids = set()
    for values_set in landmanagement.values():
        all_ids = all_ids.union(values_set)
        if len(values_set) > 1:
            overlap_ids = overlap_ids.union(values_set)
            #print(f"These values added to overlap_ids: {values_set}, {overlap_ids}")

    #print(f"Overlap_ids : {overlap_ids}")
    no_overlap_ids = all_ids - overlap_ids
    return no_overlap_ids


if __name__ == '__main__':
    main()
