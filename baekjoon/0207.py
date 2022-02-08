# https://www.acmicpc.net/problem/1181

n = int(input())
words = []
for _ in range(n):
    words.append(input())
words = list(set(words)) # 중복제거
words.sort() # 미리 sort 해놓으면 알파벳 순으로 정렬된 상태 유지
a = sorted(words, key = lambda x : len(x)) # 길이에 따라 정렬
for word in a:
    print(word)


# https://www.acmicpc.net/problem/11650

n = int(input())
points = []
for _ in range(n):
    a,b = map(int,input().split())
    points.append([a,b])
ans = sorted(points, key = lambda x: (x[0],x[1]))
for i in range(n):    
    print(ans[i][0],ans[i][1])