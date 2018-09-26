import copy

arr = [7,4,9,2,1,0,5,7,3]

def QuickSort(a, b):
    if a > b:
        return
    left = a
    right = b
    flag = arr[b]
    while left != right :
        while (arr[left] <= flag and left < right):
            left += 1
        while (arr[right] >= flag and left < right):
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[b] = arr[right]
    arr[right] = flag
    QuickSort(right+1, b)
    QuickSort(a, right-1)
    
if __name__ == '__main__':
    QuickSort(0, 8)
    print arr


