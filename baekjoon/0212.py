# https://www.acmicpc.net/problem/11004

import sys
n,k = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
print(nums[k-1])