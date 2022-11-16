def binarySearch(list, value, start, end):
    if start > end: return -1
    mid = int((start + end) / 2)
    if list[mid] == value: return mid
    if list[mid] < value: return binarySearch(list, value, mid+1, end)
    return binarySearch(list, value, start, mid-1)

list = [1, 2, 3, 4, 5, 6]
value = int(input("Enter value to be searched: "))
index = binarySearch(list, value, 0, len(list)-1)

if index == -1:
    print("Element not found")
else:
    print("Element found")
