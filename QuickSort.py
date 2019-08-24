def partition(arr, start, end):
    pivot = arr[end]
    swap = start - 1
    for scan in range(start, end):
        if arr[scan] <= pivot:
            swap += 1
            arr[swap], arr[scan] = arr[scan], arr[swap]

    arr[swap + 1], arr[end] = pivot, arr[swap + 1]
    return swap + 1


def quickSort(arr, start, end):
    if start < end:
        index = partition(arr, start, end)
        quickSort(arr, start, index - 1)
        quickSort(arr, index + 1, end)
