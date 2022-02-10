# https://www.acmicpc.net/problem/1010

import sys

# 조합의 수를 구하는 함수를 생성
def mCn(n,m):
    if m-n < n: n=m-n
    k=n
    up = 1
    down = 1
    for _ in range(k):
        up=up*m
        m-=1
    for _ in range(k):
        down=down*n
        n-=1
    print(int(up/down))
    return

cnt = int(input())
for _ in range(cnt):
    n,m = map(int,sys.stdin.readline().split())
    mCn(n,m)
