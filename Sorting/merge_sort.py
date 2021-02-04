'''
CS 5003 - Lab 8
Xiamiao Lin
'''
'''
    Test Case1: [2, 3, 5, 7, 11, 4, 6, 8], return [2, 3, 5, 7, 11, 4, 6, 8]
    Test Case2: [9, 11, 2, 5, 3, 10, 4, 6], return [2, 3, 4, 5, 6, 9, 10, 11]
    Test Case3: [8, 17, 27, 23, 15, 40], return [8, 15, 17, 23, 27, 40]
    Test Case4: [36, 40, 7, 40, 3, 22], return [3, 7, 22, 36, 40, 40]
    Test Case5: [25, 29, 20, 13, 22, 4], return [4, 13, 20, 22, 25, 29]
'''


def merge(a, b):
    result = []
    index1 = 0
    index2 = 0
    res_index = 0
    while index1 < len(a) and index2 < len(b):
        if a[index1] <= b[index2]:
            result.append(a[index1])
            index1 += 1
        else:
            result.append(b[index2])
            index2 += 1
    result += a[index1:]
    result += b[index2:]
    return result


def merge_sort(array):
    print("splitting", array)
    # base case
    if len(array) <= 1:
        return array
    mid = (len(array) + 1) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    sorted_array = merge(left, right)
    print("merging result:", sorted_array)
    return sorted_array


def main():
    print(merge_sort([2, 3, 5, 7, 11, 4, 6, 8]))
    print(merge_sort([9, 11, 2, 5, 3, 10, 4, 6]))
    print(merge_sort([8, 17, 27, 23, 15, 40]))
    print(merge_sort([36, 40, 7, 40, 3, 22]))
    print(merge_sort([25, 29, 20, 13, 22, 4]))


main()
