# https://www.acmicpc.net/problem/9625

k = int(input())
# A -> B
# B -> BA
# 다음 A의 갯수 : 현재 B의 갯수
# 다음 B의 갯수 : 현재 A의 갯수 + B의 갯수
a,b=1,0
for _ in range(k):
    next_a = b
    next_b = a + b
    a = next_a
    b = next_b
print(f'{a} {b}')