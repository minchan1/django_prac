# https://programmers.co.kr/learn/courses/30/lessons/42885

# 시간초과
# pop(0)은 데이터를 지우고 한칸씩 앞으로 당겨오기 때문에
# O(1)이 아닌 O(n)이 됨.
def solution(people, limit):
    people.sort()
    cnt=0
    # 최솟값(맨앞)과 최댓값(맨뒤)의 합이
    # limit 이하이면 둘을 태움
    # 그렇지 않으면, 최댓값 한명만 태움
    while people:
        if len(people)>=2 and people[-1]+people[0]<=limit:
            people.pop(0)
            people.pop()
            cnt += 1
        else:
            people.pop()
            cnt += 1
    return cnt

# deque를 활용
from collections import deque
def solution(people, limit):
    people = deque(sorted(people))
    cnt=0
    while people:
        if len(people)>=2 and people[-1]+people[0]<=limit:
            people.pop()
            people.popleft()
        else:
            people.pop()
        cnt += 1
    return cnt
