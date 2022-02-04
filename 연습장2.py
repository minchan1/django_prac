
from sys import stdin
from collections import deque
n = int(stdin.readline())
nums = []
for i in range(n):
    nums.append(int(stdin.readline()))
nums = deque(sorted(nums))
for i in range(n):
    print(nums.popleft())


# from collections import deque
# n = int(input())
# nums = deque()
# for i in range(n):
#     nums.append(int(input()))
# nums.sort()
# for i in range(n):
#     print(nums.popleft())