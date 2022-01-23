# https://programmers.co.kr/learn/courses/30/lessons/42862
# 설명 생략

def solution(n, lost, reserve):
    total = [1]*(n+2)
    for i in lost:
        total[i]=0
    for j in reserve:
        total[j]=2
        if j in lost:
            total[j]=1
    for k in range(1,len(total)):
        if total[k]==0:
            if total[k-1]==2:
                total[k-1] -= 1
                total[k] += 1
            elif total[k+1]==2:
                total[k+1] -= 1
                total[k] += 1
    answer=0
    for m in total:
        if m >=1 :
            answer +=1
    return answer-2

# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    a = a-1
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month_31 = [1,3,5,7,8,10,12]
    month_30 = [4,6,9,11]
    month_29 = [2]
    while a!=0:
        if a in month_31:
            a -= 1
            b += 31
        elif a in month_30:
            a -= 1
            b += 30
        else :
            a -= 1
            b += 29
    return day[b%7]