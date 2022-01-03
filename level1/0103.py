# https://programmers.co.kr/learn/courses/30/lessons/86051
# 0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. 
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 
# 더한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/87389
# 자연수 n이 매개변수로 주어집니다. 
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 
# 답이 항상 존재함은 증명될 수 있습니다.

def solution(n):
    x = 1
    while True:
        if n%x == 1:
            return x
        else:
            x += 1