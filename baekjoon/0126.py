# 그리디
# https://www.acmicpc.net/problem/1789

n = 0
s = int(input())
while s>=0:
    n += 1
    s = s-n
print(n-1)


# DP
# https://www.acmicpc.net/problem/10870

fibo = [0,1]
n=int(input())
for i in range(n):
        fibo.append(fibo[i] + fibo[i+1])
print(fibo[n])