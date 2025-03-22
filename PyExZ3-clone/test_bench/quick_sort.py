import time

def quickSort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quickSort(myList, start, pivot-1)
        quickSort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

# A more efficient solution
def quicksortBetter(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortBetter(left) + middle + quicksortBetter(right)

def test_quick_sort():
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    sorted_list = quickSort(List.copy(), 0, len(List) - 1)
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 9], f"Failed for quickSort: {sorted_list}"
    sorted_list_better = quicksortBetter(List.copy())
    assert sorted_list_better == [1, 2, 3, 4, 5, 6, 7, 9], f"Failed for quicksortBetter: {sorted_list_better}"

def main():
    test_quick_sort()

    List = [3, 4, 2, 6, 5, 7, 1, 9]
    start = time.time()
    print('Sorted List (quickSort):', quickSort(List.copy(), 0, len(List) - 1))
    stop = time.time()
    print('Time Required (quickSort):', (stop - start))
    
    start = time.time()
    print('Sorted List (quicksortBetter):', quicksortBetter(List.copy()))
    stop = time.time()
    print('Time Required (quicksortBetter):', (stop - start))

if __name__ == '__main__':
    main()

