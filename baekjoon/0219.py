# https://www.acmicpc.net/problem/2693

n = int(input())
for _ in range(n):
    tmp = list(map(int,input().split()))
    tmp.sort(reverse=True)
    print(tmp[2])
