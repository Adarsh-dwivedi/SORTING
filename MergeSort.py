def merge(arr, start, mid, end):
    duparr1 = arr[start:mid+1]
    duparr2 = arr[mid+1:end+1]
    i, j = 0, 0
    l1, l2 = len(duparr1), len(duparr2)

    for k in range(start, end+1):
        if i == l1:
            arr[k] = duparr2[j]
            j += 1
        elif j == l2:
            arr[k] = duparr1[i]
            i += 1
        elif duparr1[i] <= duparr2[j]:
            arr[k] = duparr1[i]
            i += 1
        elif duparr2[j] < duparr1[i]:
            arr[k] = duparr2[j]
            j += 1

def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr,start, mid, end)