# https://www.acmicpc.net/problem/10814

n = int(input())
tmp = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    tmp.append([age,name])
ans = sorted(tmp, key=lambda x: x[0])
for i in range(n):    
    print(ans[i][0],ans[i][1])

# https://www.acmicpc.net/problem/1158

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
lst = deque(list(range(1, n+1)))

result = []
while lst:
    for _ in range(k-1):
        lst.rotate(-1)
    result.append(str(lst.popleft()))

print("<"+', '.join(result)+">")

# https://programmers.co.kr/learn/courses/30/lessons/42584

# 시간초과
def solution(prices):
    ans = []
    for i in range(len(prices)-1):
        current = prices[i]
        for lower in prices[i+1:]:
            if min(prices[i+1:])>=current:
                ans.append(len(prices[i+1:]))
                break
            elif lower < current:
                k = prices[i+1:].index(lower)
                ans.append(k+1)
                break
    ans.append(0)
    return ans

# 통과
def solution(prices):
    ans = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt+=1
            if prices[j] < prices[i]:
                break
        ans.append(cnt)
    return ans

# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    cnt = len(citations)
    h = 0
    cnt_other = 0
    ans = []
    for _ in range(max(citations)+1):
        if cnt>=h and cnt_other <=h:
            ans.append(h)
        else:
            return ans[-1]
        cnt -= citations.count(h)
        cnt_other += citations.count(h)
        h+=1
    return ans[-1]