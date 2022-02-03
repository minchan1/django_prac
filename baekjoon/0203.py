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