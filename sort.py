""" Name: Matthew Strange
    Class: CS2420
    Date: 01/26/2021

    Description: This project implements the linear search, the binary search, and the jump search to compare their
    efficiency ins searching.
"""

import random


def quicksort(lyst, low=0, high=None):
    def partition(lyst, low, high):
        i = (low - 1)
        pivot = lyst[high]

        for x in range(low, high):
            if lyst[x] <= pivot:
                i = i + 1
                lyst[i], lyst[x] = lyst[x], lyst[i]

        lyst[i + 1], lyst[high] = lyst[high], lyst[i + 1]
        return i + 1, lyst

    if high is None:
        high = len(lyst) - 1
    if low < high:
        pivot, lyst = partition(lyst, low, high)

        quicksort(lyst, low, pivot-1)
        quicksort(lyst, pivot+1, high)
    return lyst


def mergesort(lyst):
    pass

def selection_sort(lyst):
    pass

def insertion_sort(lyst):
    pass

def is_sorted(lyst):
    testList = lyst[:]
    testList.sort()
    if testList == lyst and all(isinstance(x, int) for x in lyst):
        return True
    return False


def main():
    lyst = random.sample(range(100000000), k=10000000)
    quicksort(lyst)


if __name__ == "__main__":
    main()
