# https://programmers.co.kr/learn/courses/30/lessons/77884
# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**(1/2)) != i**(1/2):
            answer += i
        elif int(i**(1/2)) == i**(1/2):
            answer -= i
    return answer