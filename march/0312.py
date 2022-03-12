# https://www.acmicpc.net/problem/1049

import sys

n,m = map(int,sys.stdin.readline().split())
price_6 = []
price_1 = []
# 6개의 가격과 1개의 가격을 각각 리스트에 넣음
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    price_6.append(a)
    price_1.append(b)

ans = 0
# 6개세트 가격이 1개를 6개 사는것보다 저렴한 경우
# 가능한 많이 6개세트를 삼
if min(price_6) < min(price_1) * 6:
    ans += min(price_6)*(n//6)
    n = n%6
    
# 남은 n에 대하여 6개세트를 사는것과 1개를 n번 사는것을 비교
    if n*min(price_1) < min(price_6):
        ans += n*min(price_1)
    else:
        ans += min(price_6)

# 6개세트 가격이 1개를 6개 사는것보다 비싼 경우
# 1개짜리를 n개 만큼 삼
else:
    ans += min(price_1)*n
print(ans)