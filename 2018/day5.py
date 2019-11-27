import doctest
import common
import logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO)

day = 5
def main():
    #exampledata, data = common.opendata()
    datafile = f"./day{day}_input.txt"
    data = open(datafile, 'r').readlines()[0]

    print(part1(data))
    print(part2(data))


def part1(inputdata: str):
    """

    :param inputdata:
    :return:

    Example:
    >>> part1("dabAcCaCBAcCcaDA")
    10

    """
    return len(_reactpolymer(inputdata))


def _reactpolymer(polymer: str):
    """

    :param polymer:
    :return:

    Example:
    >>> _reactpolymer("dDbAaBc")
    'c'
    >>> _reactpolymer("dabAcCaCBAcCcaDA")
    'dabCBAcaDA'
    """
    return _faster_reactpolymer(polymer)


def _faster_reactpolymer(polymer: str, indice=0):
    # Only go through once, but whenever a deletion is made, check if new boundaries also get a deletion

    if len(polymer) <= indice + 1:
        return polymer

    i = 0
    isrev = _isreversecase
    p = polymer
    while i < len(p) - 1:
        logging.debug(f"p: {p}")
        if isrev(p[i], p[i+1]):
            p = p[:i] + p[i+2:]
            i -= 1 if i > 0 else 0
        else:
            i += 1
    polymer = p
    return polymer


def _brute_reactpolymer(polymer):
    # Brute force loop through and pop until a full loop without pops can be made
    pop = True
    reduced_polymer = []
    polymer = list(polymer)
    while pop:
        pop = False
        if len(polymer) == 1:
            return polymer[0]
        for i in range(len(polymer[:-1])):
            a = polymer[i]
            b = polymer[i+1]
            logging.debug(f'Checking a,b: {a}, {b}')
            if _isreversecase(a, b):
                logging.debug(f'a,b found: {a}, {b}')
                indice = i
                pop = True
                break
        if not pop:
            break
        logging.debug(f'Popping indice {indice}')
        polymer.pop(indice)
        polymer.pop(indice)
    return ''.join(polymer)


def _isreversecase(a, b):
    """

    :param a:
    :param b:
    :return:

    Example:
    >>> _isreversecase('a', 'A')
    True
    >>> _isreversecase('B', 'b')
    True
    >>> _isreversecase('A', 'A')
    False
    >>> _isreversecase('a', 'a')
    False
    >>> _isreversecase('z', 'W')
    False
    >>> _isreversecase('z', '5')
    Traceback (most recent call last):
    ValueError: Invalid input for letters: z, 5
    """
    if not (('A' <= a.upper() <= 'Z') and ('A' <= b.upper() <= 'Z')):
        raise ValueError(f"Invalid input for letters: {a}, {b}")
    elif a == b:
        return False
    elif a.upper() != b.upper():
        return False
    else:
        return True


def part2(data):
    """

    :param data:
    :return:

    >>> part2("dabAcCaCBAcCcaDA")
    4
    """
    baseset = set(data.lower())
    bestreductionletter = ""
    bestreduction = len(data)

    for base in baseset:
        logging.debug(f"Trying base {base}")
        reduceddata = data.replace(base, '').replace(base.upper(), '')
        reduction = part1(reduceddata)
        if reduction < bestreduction:
            logging.debug(f"New best: {bestreductionletter}, amount: {bestreduction}")
            bestreduction = reduction
            bestreductionletter = base

    return bestreduction


if __name__ == '__main__':
    main()