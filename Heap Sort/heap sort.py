# heapify array into binary heap(Max heap used)
def heapify(arr, N, idx):
    max_idx = idx
    left, right = idx * 2 + 1, idx * 2 + 2
    if left < N and arr[left] > arr[max_idx]:
        max_idx = left
    if right < N and arr[right] > arr[max_idx]:
        max_idx = right

    if max_idx != idx:
        arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
        heapify(arr, N, max_idx)


# implement heap sort
def heap_sort(arr):
    # count number of node
    num_of_node = int(len(arr) / 2)
    last = len(arr)

    # initialize max heap backwardly
    for i in range(num_of_node - 1, -1, - 1):
        heapify(arr, last, i)

    # Iteratively get maximum value in O(1) time
    # Swap with leaf element(unstable)
    # Maintain Max heap structure by heapify function
    while last > 1:
        arr[0], arr[last - 1] = arr[last - 1], arr[0]
        last -= 1
        heapify(arr, last, 0)

# testing
if __name__ == '__main__':
    arr = [3, 1, 24, 12, 252, 7, 2]
    heap_sort(arr)
    print('Sorted array is: ')
    for i in range(len(arr)):
        print('%d' % arr[i], end=' ')
