# https://programmers.co.kr/learn/courses/30/lessons/12941

from collections import deque
def solution(A,B):
    A = deque(sorted(A))
    B = deque(sorted(B))
    ans=0
    # 결과값이 최소가 되려면 큰수와, 작은수를 곱하여 더해야함
    for _ in range(len(A)):
        ans += A.popleft()*B.pop()
    return ans