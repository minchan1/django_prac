# https://www.acmicpc.net/problem/11652

import sys

n = int(sys.stdin.readline())
nums = {}
for _ in range(n):
    k = int(sys.stdin.readline())
    if k in nums:
        nums[k] += 1
    else:
        nums[k] = 1
ans = sorted(nums.items(), key=lambda x: (-x[1], x[0]))
print(ans[0][0])
