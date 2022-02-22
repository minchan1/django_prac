# https://www.acmicpc.net/problem/11931

import sys
n = int(sys.stdin.readline())
tmp = []
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))
tmp.sort()
for _ in range(n):
    print(tmp.pop())