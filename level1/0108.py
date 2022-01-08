# https://programmers.co.kr/learn/courses/30/lessons/12921
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

def solution(n):
    answer = 0
    nums = []
    for a in range(2,n+1):
        nums.append(a)
    for k in nums:
        if k ==2 :
            answer += 1
        for i in range(2,k):
            if k%i == 0:
                break
            else :
                if i == k-1:
                    answer += 1
                else :
                    continue 
    return answer