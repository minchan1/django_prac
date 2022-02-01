# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    cnt = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        # 더이상 조합할 수 없으면 -1 출력
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, (a+(b*2)))
            cnt += 1
        # 최소값 두개를 뽑아 조합
    return cnt

# 그리디
# https://www.acmicpc.net/problem/2217

n = int(input())
ropes=[]
for i in range(n):
    ropes.append(int(input()))
ropes=sorted(ropes)
wei = 0
# 중량이 작은 로프부터 n개씩
for i in ropes:
    if i*n>wei:
        wei=i*n
        n-=1
    else:
        n-=1
print(wei) 

# 그리디
# https://www.acmicpc.net/problem/10610

n = list(input())
sum_ = 0
for i in n:
    sum_ += int(i)
# 각 자리 숫자를 더한값이 3의 배수이고,
# 0이 포함되어야만 30의 배수가 될 수 있다
if sum_%3==0 and '0' in n:
    n = sorted(n)
    ans = ''
    for i in range(len(n)):
        ans=ans+n.pop()
    # 오름차순으로 정리하고 맨뒤(가장 큰 수)부터 이어붙임
    print(ans)
else:
    print(-1)