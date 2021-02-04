'''
CS 5001 - Lab 7
Xiamiao Lin
Programming 1
'''
'''
    Test Case1: nums = [6, 13, 21, 22, 41, 49, 51],  target = 49, return 5
    Test Case2: nums = [11, 22, 17, 31, 45, 56, 70], target = 31, return 3
    Test Case3: nums = [1, 2, 3, 4, 5, 6], target 8, return none
    Test Case4: nums = [23, 33, 35, 64, 89, 100], target = 33, return 1
    Test Case5: nums = [1, 37, 39, 59, 83, 98], target = 1, return 0
'''


def sequentialSearch(nums, target):
    """
    Parameters: list of nums, int, target, an int
      Returns: index, int
    Does: return index of the target number in the list, if not found, return
    None
    """
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return None


def main():
    nums1 = [6, 13, 21, 22, 41, 49, 51]
    nums2 = [11, 22, 17, 31, 45, 56, 70]
    nums3 = [1, 2, 3, 4, 5, 6]
    nums4 = [23, 33, 35, 64, 89, 100]
    nums5 = [1, 37, 39, 59, 83, 98]
    print(sequentialSearch(nums1, 49))
    print(sequentialSearch(nums2, 31))
    print(sequentialSearch(nums3, 8))
    print(sequentialSearch(nums4, 33))
    print(sequentialSearch(nums5, 1))


main()
