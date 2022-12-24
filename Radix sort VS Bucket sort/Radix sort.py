# Radix sort using radix 10
def radix_sort(nums):
    max_num = max(nums)
    exp = 1

    while max_num / exp > 0:
        count = [0] * 10
        output = [0] * len(nums)

        # build-up counting-sort subroutine
        for num in nums:
            index = int(num / exp) % 10
            count[index] += 1

        # get last occurrence index(stable)
        for i in range(1, 10):
            count[i] += count[i - 1]

        # sort nums array in kth digit
        for j in range(len(nums) - 1, -1, -1):
            idx = int(nums[j] / exp) % 10
            output[count[idx] - 1] = nums[j]
            count[idx] -= 1

        # cache intermediate sorted number list
        for k in range(len(nums)):
            nums[k] = output[k]

        exp *= 10

# testing
if __name__ == '__main__':
    nums = [3, 24151, 1, 156, 26, 928, 78, 199]
    radix_sort(nums)

    print('sorted array is: ')
    for i in range(len(nums)):
        print('%d' % nums[i], end=' ')
