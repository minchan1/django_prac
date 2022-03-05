# https://www.acmicpc.net/problem/2164

from collections import deque

# deque를 사용해서 리스트를 더 효율적으로 수정
n = int(input())
if n==1:
    print(1)
else:
    tmp = [i+1 for i in range(n)]
    deq = deque(tmp)
    while True:
        deq.popleft()
        if len(deq) == 1:
            break
        deq.append(deq.popleft())
    print(deq[0])