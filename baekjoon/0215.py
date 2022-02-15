# https://www.acmicpc.net/problem/1439

S = list(input())
tmp = [S[0]]
for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        tmp.append(S[i+1])
ans = min(tmp.count('1'),tmp.count('0'))
print(ans)