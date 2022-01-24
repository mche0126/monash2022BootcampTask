import array


def bubbleSort(arr: array):
    """
    This method is bubble sort method, is the basic sorting algorithm which will be required in sorting

    :param arr:  An list object which contains some numbers which need to be sorted
    :return: arr: The sorted array object
    """
    # Get the length of the array [how many number is inside]
    n = len(arr)

    # Create loops to compare numbers, i is for the round and j is for the comparing element
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Check the neighbor element, if left is larger than right, then swamp them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    """
    This is the main function of the script, which should include all process in the script

    :return:
    """
    arr = [5, 1, 3, 2, 10, 7]
    sorted_arr = bubbleSort(arr)
    print(sorted_arr)


if __name__ == "__main__":
    main()
