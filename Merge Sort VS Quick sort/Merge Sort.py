# Implement Merge Sort Algorithm, time complexity O(nlog(n)), space O(n)
def merge_sort(arr):
    # stopping criteria
    if len(arr) == 1:
        return [arr[0]]

    if len(arr) == 0:
        return

    # create stack top-down
    left, right = 0, len(arr)
    mid = (left + right) // 2

    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    # complete operation and return result bottom-up
    new_arr = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            new_arr.append(L[i])
            i += 1
        elif L[i] > R[j]:
            new_arr.append(R[j])
            j += 1

    # check remaining element
    if i < len(L):
        new_arr += L[i:]

    if j < len(R):
        new_arr += R[j:]

    return new_arr

# Testing
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 8, 94, 192, 101]
    sorted_arr = merge_sort(arr)
    print(f'Sorted Array is: {sorted_arr}')