def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


arr = [4, 12, 3, 9, 7, 24, 32, 17]


def binary(list, n):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        if list[mid] == n:
            return mid
        elif list[mid] > n:
            hight = mid - 1
        else:
            low = mid + 1
    return None
