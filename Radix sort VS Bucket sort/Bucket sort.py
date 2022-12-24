# insertion sort for each bucket
def insertion_sort(arr):
    for i in range(1, len(arr)):
        up = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > up:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = up


# bucket sort
def bucket_sort(nums, num_of_bucket):
    bucket = [[] for _ in range(num_of_bucket)]
    max_num, min_num = max(nums), min(nums)
    bucket_width = (max_num - min_num) / (num_of_bucket - 1)

    # assign number into buckets(one-pass)
    for num in nums:
        idx = int((num - min_num) / bucket_width)

        bucket[idx].append(num)

    # sort each individual bucket
    for buc in bucket:
        insertion_sort(buc)

    # concatenate result in place
    k = 0
    for num_list in bucket:
        if num_list:
            for num in num_list:
                nums[k] = num
                k += 1


# testing
if __name__ == '__main__':
    nums = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

    bucket_sort(nums, 10)
    print('Sorted number is: ')
    print(nums)
