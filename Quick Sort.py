import array


def quick_sort(arr: array, left: int, right: int):
    """
    This is a quick sort method, using algorithm to reduce the computational steps.
    This method will use recurrent method to sort the array
    :param arr: The array waiting for sorting
    :param left: The left edge for current sort
    :param right: The right edge for current sort
    :return: arr: The sorted array for this sort
    """

    # Stop iteration when left pointer is larger than right one
    if left >= right:
        return

    # Set index as left edge index
    low = left

    # Set index as right edge index
    high = right

    # Set pivot value as low index value
    key = arr[low]

    #  iterate when left pointer is less than right pointer
    while left < right:
        # narrow right pointer when right value is larger than pivot value and switch the left and right partition
        while left < right and arr[right] > key:
            # right = right - 1
            right -= 1
        arr[left] = arr[right]

        # similar as upper part
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]

    #  refresh the pivot value
    arr[right] = key
    quick_sort(arr, low, left - 1)
    quick_sort(arr, left + 1, high)

    return arr


def main():
    arr = [2, 5, 4, 9, 3, 1]
    print(quick_sort(arr, 0, len(arr) - 1))


if __name__ == "__main__":
    main()
