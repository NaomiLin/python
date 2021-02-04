def find_pivot(array, left, right):
    pivot = array[left]
    i = left + 1
    j = len(array) - 1
    while i < j:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    array[left], array[j] = array[j], array[left]
    print(array, j)
    return j


def quick_sort(array, left, right):
    if left >= right:
        return
    pivot = find_pivot(array, left, right)
    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot + 1, right)


def main():
    arr = [5, 2, 3, 1]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


main()
