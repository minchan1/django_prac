# https://www.acmicpc.net/problem/1920

n = int(input())
nums = list(map(int, input().split()))
nums.sort()


# 이진탐색 활용
def binary_search(arr, value):
    first, last = 0, len(arr)-1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            last = mid - 1
        else:
            first = mid + 1
    return -1


m = int(input())
b = list(map(int, input().split()))
for num in b:
    if binary_search(nums, num) >= 0:
        print(1)
    else:
        print(0)
