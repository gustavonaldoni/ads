def swap(array: list[int], i: int, j: int) -> None:
    temp = array[j]
    array[j] = array[i]
    array[i] = temp


def bubble_sort(array: list[int]) -> None:
    array_length = len(array)

    for i in range(0, array_length - 1):
        for j in range(0, array_length - 1 - i):
            if array[i] > array[j]:
                swap(array, i, j)
