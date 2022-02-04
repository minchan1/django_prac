# 구현
# https://www.acmicpc.net/problem/1316

import string
lower = [i for i in string.ascii_lowercase]
n = int(input())
cnt = 0
words = []
for _ in range(n):
    words.append(input() + '0')
for word in words:
    tmp = []
    for i in range(len(word)-1):       
        if word[i]!=word[i+1] and word[i] not in tmp:
            tmp.append(word[i])
    if len(tmp) == len(set(word))-1:
        cnt += 1
print(cnt)

# 스택,큐
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    remain = []
    result = []
    cnt = []
    for i in range(len(progresses)):
        tmp=(100-progresses[i])/speeds[i]
        if int(tmp) == tmp:
            remain.append(int(tmp))
        else:
            remain.append(int(tmp)+1)
    for i in range(len(remain)):
        if result:
            if result[0]>=remain[i]:
                result.append(remain[i])
            else:
                cnt.append(len(result))
                result.clear()
                result.append(remain[i])
        else:
            result.append(remain[i])
    if result:
        cnt.append(len(result))
    return cnt