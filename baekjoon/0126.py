# 그리디
# https://www.acmicpc.net/problem/1789

n = 0
s = int(input())
while s>=0:
    n += 1
    s = s-n
print(n-1)