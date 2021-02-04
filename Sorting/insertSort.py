'''
CS 5001 - Lab 7
Xiamiao Lin
Programming 5
'''
'''
    Test Case1: nums1 = [29, 41, 96, 0, 58, 51, 38],
                print: [0, 29, 38, 41, 51, 58, 96]
    Test Case1: nums2 = [27, 99, 72, 38, 31, 46, 87]
                print: [27, 31, 38, 46, 72, 87, 99]
    Test Case1: nums3 = [46, 4, 28, 71, 79, 49, 31]
                print: [4, 28, 31, 46, 49, 71, 79]
    Test Case1: nums4 = [93, 79, 97, 19, 1, 7, 4]
                print: [1, 4, 7, 19, 79, 93, 97]
    Test Case1: nums5 = [30, 16, 22, 34, 67, 72, 28]
                print: [16, 22, 28, 30, 34, 67, 72]
'''


def insertionSort(nums):
    """
    Parameters: list of nums, int
      Returns: None
    Does: Print the nums after insetSort
    """
    n = len(nums)
    for i in range(1, n):
        insertNum = nums[i]
        # sorted sublist's last index
        index = i - 1
        # traverse from end to start, if insert number is smaller than last
        # number of the sorted sublist, do while loop
        while index >= 0 and insertNum < nums[index]:
            # shift each number in the sorted sublist to the right until we
            # fing the right position for the insert number
            nums[index + 1] = nums[index]
            index -= 1
        nums[index + 1] = insertNum
    print(nums)


def main():
    nums1 = [29, 41, 96, 0, 58, 51, 38]
    nums2 = [27, 99, 72, 38, 31, 46, 87]
    nums3 = [46, 4, 28, 71, 79, 49, 31]
    nums4 = [93, 79, 97, 19, 1, 7, 4]
    nums5 = [30, 16, 22, 34, 67, 72, 28]
    insertionSort(nums1)
    insertionSort(nums2)
    insertionSort(nums3)
    insertionSort(nums4)
    insertionSort(nums5)


main()
