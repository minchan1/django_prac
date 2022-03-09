# https://www.acmicpc.net/problem/1157

word = list(str(input()).upper())
tmp = list(set(word))
cnt = []

for i in tmp:
    cnt.append(word.count(i))
if cnt.count(max(cnt))!=1:
    print('?')
else:   
    k = max(cnt)
    n = cnt.index(k)
    print(tmp[n]) 