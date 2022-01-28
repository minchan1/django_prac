# https://programmers.co.kr/learn/courses/30/lessons/72410


def solution(new_id):
    temp = list(new_id)
    result = []
    ok = ['-','_','.']
    for i in range(len(temp)):
        temp[i] = temp[i].lower()   # 1단계
        if temp[i] in ok or temp[i].isalnum()==True:  # 2단계
            result.append(temp[i])
    for i in range(len(result)-1):
        if result[i] == '.' and result[i+1]=='.':
            result[i]='?'
    while '?' in result:
        result.remove('?')  # 3단계
    if result:
        if result[0] == '.': 
                del result[0]
    if result:
        if result[-1] == '.':
                del result[-1]   # 4단계
    if not result:
        result.append('a') # 5단계
    if len(result)>=16:
        del result[15:] # 6단계
    if result[-1] == '.':
        del result[-1]   # 6-1단계
    while len(result)<=2:
        result.append(result[-1]) # 7단계
    return ''.join(result)

# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    rate = {}
    p = len(stages)
    for i in range(1,N+1):
        if p ==0:
            ratio=0
        else:
            ratio=stages.count(i)/p
            p-=stages.count(i)
        rate[i] = ratio   # 각 스테이지의 실패율을 구함
    result = sorted(rate.items(), key=lambda x : x[1], reverse=True)  # value값이 높은순서로 정렬
    ans = []
    for i in range(N):
        ans.append(result[i][0])
    return(ans)