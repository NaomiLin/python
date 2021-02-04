'''
CS 5001 - Lab 7
Xiamiao Lin
Programming 4
'''
'''
    Test Case1: nums1 = [29, 41, 96, 0, 58, 51, 38],
                print: [0, 29, 38, 41, 51, 58, 96]
    Test Case2: nums2 = [27, 99, 72, 38, 31, 46, 87]
                print: [27, 31, 38, 46, 72, 87, 99]
    Test Case3: nums3 = [46, 4, 28, 71, 79, 49, 31]
                print: [4, 28, 31, 46, 49, 71, 79]
    Test Case4: nums4 = [93, 79, 97, 19, 1, 7, 4]
                print: [1, 4, 7, 19, 79, 93, 97]
    Test Case5: nums5 = [30, 16, 22, 34, 67, 72, 28]
                print: [16, 22, 28, 30, 34, 67, 72]
'''


def selectionSort(nums):
    """
    Parameters: list of nums, int
      Returns: None
    Does: Print the nums after selectionSort
    """
    n = len(nums)
    for i in range(n):
        maxIndex = 0
        # each inner loop, the size decrease by 1 since we move 1 number to the
        # rightmost
        for j in range(0, n - i):
            # find the largest number's index
            if nums[j] > nums[maxIndex]:
                maxIndex = j
        # swap, the largest number will be moved to last index of unsorted list
        nums[j], nums[maxIndex] = nums[maxIndex], nums[j]
    print(nums)


def main():
    nums1 = [29, 41, 96, 0, 58, 51, 38]
    nums2 = [27, 99, 72, 38, 31, 46, 87]
    nums3 = [46, 4, 28, 71, 79, 49, 31]
    nums4 = [93, 79, 97, 19, 1, 7, 4]
    nums5 = [30, 16, 22, 34, 67, 72, 28]
    selectionSort(nums1)
    selectionSort(nums2)
    selectionSort(nums3)
    selectionSort(nums4)
    selectionSort(nums5)


main()
