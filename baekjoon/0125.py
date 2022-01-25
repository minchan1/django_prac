# 그리디
# https://www.acmicpc.net/problem/11047

n,k = map(int,input().split())
coin = []
count = 0 
for _ in range(n): 
	coin.append(int(input()))
for i in range(-1,-n-1,-1):
    if coin[i] <= k:
        count += k//coin[i]
        k = k%coin[i]
print(count)

# 그리디
# https://www.acmicpc.net/problem/1026

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a)
b = sorted(b)
b.reverse()
s=0
for i in range(n):
    s += a[i]*b[i]
print(s)

# 브루트포스
# https://www.acmicpc.net/problem/2798

import itertools
n,m = map(int,input().split())
cards = list(map(int,input().split()))
li = list(itertools.combinations(cards,3))
for i in range(len(li)):
    li[i] = li[i][0] + li[i][1] + li[i][2]
li = set(sorted(li))
li = list(li)
nums = []
for i in range(len(li)):
    if li[i]>m:
        nums.append(li[i])
for i in range(len(nums)):
    li.remove(nums[i])
print(max(li))