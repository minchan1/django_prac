# https://www.acmicpc.net/problem/10815

import sys
n = int(sys.stdin.readline())
nums = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
tmp = list(map(int,sys.stdin.readline().split()))
for i in tmp:
    if i in nums:
        print(1,end=' ')
    else:
        print(0,end=' ')