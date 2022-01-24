import array


def selection_sort(arr: array):
    """
    This method is selection sort method, the idea is select the minimum number in an array
    and put it to the first place
    :param arr: Array waiting for selection
    :return: Array after sorting
    """
    for i in range(len(arr)):
        # Get the current first number
        first_place = i

        # iterate through the arr and replace the index with the lowest value
        for j in range(i + 1, len(arr)):
            if arr[first_place] > arr[j]:
                first_place = j

        # switch the first place value with the lowest value
        arr[i], arr[first_place] = arr[first_place], arr[i]

    return arr


def main():
    arr = [5, 2, 3, 4, 10, 6]
    # print the results
    print(selection_sort(arr))


if __name__ == "__main__":
    main()
