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

# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    n = len(arr2[0])
    m = len(arr1)
    result= [[0]*n for i in range(m)]
    tmp=0
    for i in range(m):
        for j in range(n):
            for k in range(len(arr1[0])):
                tmp += arr1[i][k]*arr2[k][j]
            result[i][j]=tmp
            tmp=0
    return result

# https://programmers.co.kr/learn/courses/30/lessons/12909

# 효율성1 실패
from collections import deque
s = "(())()"
s = deque(s)
if s.count('(') != s.count(')'):
    print('False')
elif s[0]==')' or s[-1]=='(':
    print('False')
else:
    while s:
        if s[0]==')':
            print('False')
            break   
        s.popleft()
        s.remove(')')
    print('True')

# 스택 사용
def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
    return stack==[]