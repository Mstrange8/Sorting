""" Name: Matthew Strange
    Class: CS2420
    Date: 01/26/2021

    Description: This project implements the linear search,
    the binary search, and the jump search to compare their
    efficiency ins searching.
"""

import random
from time import perf_counter


"""Quick sort is done in linear Big O Notation.
It sorts by choosing a pivot point and places all smaller values to
the left of the pivot and all larger values to the right of the pivot."""


def quicksort(lyst, low=0, high=None):
    """Sorts array using quick sort method."""
    def partition(my_list, first, last):
        i = (first - 1)
        piv = my_list[last]

        for x in range(first, last):
            if my_list[x] <= piv:
                i = i + 1
                my_list[i], my_list[x] = my_list[x], my_list[i]

        my_list[i + 1], my_list[last] = my_list[last], my_list[i + 1]
        return i + 1, my_list

    def _quicksort(lyst, low, high):
        if low < high:
            pivot, lyst = partition(lyst, low, high)

            _quicksort(lyst, low, pivot-1)
            _quicksort(lyst, pivot+1, high)
        return lyst

    if all(isinstance(x, int) for x in lyst):
        if high is None:
            high = len(lyst) - 1
        return _quicksort(lyst, low, high)
    raise ValueError


""" Merge sort continuously divides the array in half until each element is separate.
Then it combines each of these elements, sorting them along the way. """


def mergesort(lyst):
    """Sorts array using merge sort method."""
    if all(isinstance(x, int) for x in lyst):
        if len(lyst) > 1:
            center = len(lyst)//2
            left = lyst[:center]
            right = lyst[center:]

            mergesort(left)
            mergesort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lyst[k] = left[i]
                    i += 1
                else:
                    lyst[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                lyst[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                lyst[k] = right[j]
                j += 1
                k += 1
        return lyst
    raise ValueError


""" Selection sort sorts the array by repeatedly finding the
minimum value and putting it at the beginning of the array."""


def selection_sort(lyst):
    """Sorts array using selection sort method."""
    if all(isinstance(x, int) for x in lyst):
        for a in range(len(lyst)):
            minVal = a
            for b in range(a+1, len(lyst)):
                if lyst[minVal] > lyst[b]:
                    minVal = b
            lyst[a], lyst[minVal] = lyst[minVal], lyst[a]
        return lyst
    raise ValueError


""" Insertion sort creates two arrays. One contains sorted values and one contains
non sorted values. The values from the non sorted array are added to the sorted array
as they get sorted."""


def insertion_sort(lyst):
    """Sorts array using insertion sort method."""
    if all(isinstance(x, int) for x in lyst):
        for i in range(1, len(lyst)):
            key = lyst[i]
            j = i-1
            while j >= 0 and key < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            lyst[j+1] = key
        return lyst
    raise ValueError


def is_sorted(lyst):
    """Tests if the passed in array is sorted."""
    if all(isinstance(x, int) for x in lyst):
        testList = lyst[:]
        testList.sort()
        if testList == lyst:
            return True
        return False
    raise ValueError


def main():
    """Print sorting run times."""

    lyst = random.sample(range(30000), k=10000)
    selection_list = lyst.copy()
    insertion_list = lyst.copy()
    merge_list = lyst.copy()
    quick_list = lyst.copy()


    """Selection Sort"""
    print("Starting selection_sort")
    start_time = perf_counter()
    selection_sort(selection_list)
    print("Selection sort duration: {:4f} seconds\n".format(perf_counter() - start_time))

    """Insertion Sort"""
    print("Starting insertion_sort")
    start_time = perf_counter()
    insertion_sort(insertion_list)
    print("Insertion sort duration: {:4f} seconds\n".format(perf_counter() - start_time))

    """Merge Sort"""
    print("Starting mergesort")
    start_time = perf_counter()
    mergesort(merge_list)
    print("Mergesort duration: {:4f} seconds\n".format(perf_counter() - start_time))

    """Quick Sort"""
    print("Starting quicksort")
    start_time = perf_counter()
    quicksort(quick_list)
    print("Quicksort duration: {:4f} seconds".format(perf_counter() - start_time))



if __name__ == "__main__":
    main()
