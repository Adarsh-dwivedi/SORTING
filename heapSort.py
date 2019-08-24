def heapify(arr, start, size):
    """This function assume that it's left and right subtree are in heap and then it build that node a heap"""
    left = 2*start + 1
    right = 2*start + 2

    largest = left if left < size and arr[left] > arr[start] else start

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != start:
        arr[start], arr[largest] = arr[largest], arr[start]  # making the largest number parent acc. to heap
        heapify(arr, largest, size)  # checking for swapped node that it is a heap or not


def build_heap(arr, size):
    """This function help to build whole tree max heap"""
    for i in range(size//2-1, -1, -1):  # size//2 gives the index of starting leaf node
        heapify(arr, i, size)


def heap_sort(arr, size):
    build_heap(arr, size)
    for i in range(size-1, 0, -1):  # size-1 helps to exclude the last node which is largest
        arr[0], arr[i] = arr[i], arr[0]  # putting the largest element at last position
        build_heap(arr, i)
