# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    temp = []
    # 리스트로 변경, 특문 없는 경우는 공백 으로
    for i in range(len(dartResult)-1):
        if dartResult[i].isalpha() == True and dartResult[i+1].isdecimal() == True:
            temp.append(dartResult[i])
            temp.append(' ')
        elif dartResult[i].isdecimal() == True and dartResult[i+1].isdecimal() == True:
            temp.append('10')
            # 숫자가 10인 경우 처리
        else:
            if dartResult[i-1].isdecimal() ==True and dartResult[i].isdecimal()==True:
                pass
            else:
                temp.append(dartResult[i])
    if dartResult[-1].isalpha() == True:    
        temp.append(dartResult[-1])
        temp.append(' ')
    else:
        temp.append(dartResult[-1])

    # 계산하기
    ans = 0 
    for i in range(len(temp)):
        if i%3==1:
            if temp[i]=='D':temp[i-1]=int(temp[i-1])**2
            elif temp[i]=='T':temp[i-1]=int(temp[i-1])**3
            elif temp[i]=='S':temp[i-1]=int(temp[i-1])**1
    for i in range(len(temp)):
        if i%3==2:
            if temp[i]=='*' and i==2:temp[i-2]=temp[i-2]*2
            elif temp[i]=='*':
                temp[i-2]=temp[i-2]*2
                temp[i-5]=temp[i-5]*2
            elif temp[i]=='#':temp[i-2]=temp[i-2]*(-1)
    for i in temp:
        if type(i)==int:
            ans += i
    return(ans)