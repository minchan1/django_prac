# 그리디
# https://www.acmicpc.net/problem/11034

# a,b,c=input().split()
# if b-a >= c-b:
#     print(b-a-1)
# else:
#     print(c-b-1)

while True:
    try:
        a,b,c = map(int, input().split())
        d = max(b-a, c-b)
        print(d-1)
    except:
        exit()