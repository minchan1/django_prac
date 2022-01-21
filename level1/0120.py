# https://programmers.co.kr/learn/courses/30/lessons/12928
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

def solution(n):
    a = 0
    for i in range(1,n+1):
        if n%i ==0: a += i
    return a


# https://programmers.co.kr/learn/courses/30/lessons/12934
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, 
# n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

def solution(n):
    if n**(1/2) == int(n**(1/2)):
        return (n**(1/2)+1)**2
    else: return -1