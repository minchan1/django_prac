# https://www.acmicpc.net/problem/10867

import sys
n = int(sys.stdin.readline())
tmp = list(map(int,sys.stdin.readline().split()))
tmp = list(set(tmp))
tmp.sort()
for i in tmp:
    print(i,end=' ')