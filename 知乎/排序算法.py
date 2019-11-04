# 以下是八大排序算法的python实现

# 冒泡排序
def bubble_sort(numlist):
    length = len(numlist)
    for i in range(length):
        for j in range(1,length - i):
            if numlist[j - 1] > numlist[j]:
                numlist[j - 1], numlist[j] = numlist[j], numlist[j - 1]
    return numlist

# 选择排序
def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectsort(arr):
    newarr = []
    while arr:
        smallest = find_Smallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

# 插入排序
def insert_sort(numlist):
    for i in range(1, len(numlist)):
        cur = numlist[i]
        j = i
        while cur < numlist[j-1] and j > 0:
            numlist[j] = numlist[j-1]
            j -= 1
        numlist[j] = cur
    return numlist

# 希尔排序
def shell_sort(numlist):
    length = len(numlist)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = numlist[i]
            j = i
            while temp < numlist[j - gap] and j > 0:
                numlist[j] = numlist[j - gap]
                j -= gap
            numlist[j] = temp
        gap = gap // 2
    return numlist

# 归并排序
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

def merge_sort(numlist):
    if len(numlist) <= 1:
        return numlist

    mid = len(numlist) // 2
    left = numlist[:mid]
    right = numlist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)



if __name__ == '__main__':
    # 冒泡排序
    numlist = [3, 5, 4, 7, 9, 6, 2, 8, 1]
    print(bubble_sort(numlist))

    # 选择排序
    numlist = [3, 5, 4, 7, 9, 6, 2, 8, 1]
    print(selectsort(numlist))

    # 插入排序
    numlist = [3, 5, 4, 7, 9, 6, 2, 8, 1]
    print(insert_sort(numlist))

    # 希尔排序
    numlist = [3, 5, 4, 7, 9, 6, 2, 8, 1]
    print(shell_sort(numlist))

    # 归并排序
    numlist = [3, 5, 4, 7, 9, 6, 2, 8, 1]
    print(merge_sort(numlist))
