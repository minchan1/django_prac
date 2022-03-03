# https://www.acmicpc.net/problem/10773

n = int(input())
tmp = []
for _ in range(n):
    k = int(input())
    if k !=0:
        tmp.append(k)
    # 0이 아닌수는 리스트에 추가
    else:
        tmp.pop()
    # 0인 경우 리스트의 맨 마지막 원소를 지움
print(sum(tmp))