'''
CS 5001 - Lab 7
Programming 3
Xiamiao Lin
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


def bubbleSort(nums):
    """
    Parameters: list of nums, int
      Returns: None
    Does: print the nums after bubleSort
    None
    """
    n = len(nums)
    for num_pass in range(n - 1):
        for i in range(n - 1 - num_pass):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(nums)


def main():
    nums1 = [29, 41, 96, 0, 58, 51, 38]
    nums2 = [27, 99, 72, 38, 31, 46, 87]
    nums3 = [46, 4, 28, 71, 79, 49, 31]
    nums4 = [93, 79, 97, 19, 1, 7, 4]
    nums5 = [30, 16, 22, 34, 67, 72, 28]
    bubbleSort(nums1)
    bubbleSort(nums2)
    bubbleSort(nums3)
    bubbleSort(nums4)
    bubbleSort(nums5)


main()
