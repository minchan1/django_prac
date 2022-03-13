# https://www.acmicpc.net/problem/1543

word = str(input())
tmp = str(input())
cnt = 0 

# word내에 tmp가 존재하면 카운트
# word를 tmp가 있던 위치의 뒤로 갱신
while word.count(tmp):
    cnt += 1
    word = word[word.index(tmp)+len(tmp):]

print(cnt)