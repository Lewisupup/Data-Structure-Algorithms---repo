# Implement Quick Sort, time complexity O(nlog(n)), space O(1) in-place
def quick_sort(arr, left, right):
    # stopping criteria
    if left < right:

        # choose most right element as pivot
        pivot = arr[right]

        # swap lower element
        low_idx = left - 1
        for i in range(left, right):
            if arr[i] <= pivot:
                low_idx += 1
                arr[low_idx], arr[i] = arr[i], arr[low_idx]

        # correct pivot position
        arr[low_idx + 1], arr[right] = arr[right], arr[low_idx + 1]
        pi = low_idx + 1

        # sort remaining part recursively
        quick_sort(arr, left, low_idx - 1)
        quick_sort(arr, low_idx + 1, right)

# Testing
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 8, 94, 192, 101]
    quick_sort(arr, 0, len(arr) - 1)
    print(f'Sorted Array is:{arr}')

# END