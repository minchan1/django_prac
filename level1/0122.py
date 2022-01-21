# https://programmers.co.kr/learn/courses/30/lessons/12943
# 콜라츠 추측 :
# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요.

def solution(num):
    n=0
    while num!=1:
        if n==500: return -1
        elif num%2==0:
            num = num/2
            n+=1      
        else:
            num = num*3 +1
            n+=1
    return n

# https://programmers.co.kr/learn/courses/30/lessons/12918
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

def solution(s):
    try:
        int(s)
        if len(s)==4 or len(s)==6: return True
        else : return False
    except: return False