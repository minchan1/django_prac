# https://www.acmicpc.net/problem/1676

def fac(n):
    k = 1
    while n:
        k = k*n
        n -= 1
    return k

n = int(input())
ans = fac(n)
tmp = list(str(ans))
cnt = 0
for i in range(-1,-len(tmp),-1):
    if tmp[i] == '0':
        cnt += 1
    else: break
print(cnt)