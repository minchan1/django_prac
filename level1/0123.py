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
