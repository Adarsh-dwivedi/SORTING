def insertionSort(unSort):

    for next in range(1, len(unSort)):
        key = unSort[next]
        prev = next-1

        while(prev>=0 and unSort[prev]>key):
            unSort[prev+1] = unSort[prev]
            prev -= 1

        unSort[prev+1] = key

a = list(range(10, 0, -1))
insertionSort(a)
print(a)

