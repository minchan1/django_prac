# https://www.acmicpc.net/problem/1357


# 자릿수를 뒤집는 함수 생성
def Rev(n):
    return int(str(n)[::-1])


# x,y에 대해 적용
x, y = map(int, input().split())
print(Rev(Rev(x)+Rev(y)))
