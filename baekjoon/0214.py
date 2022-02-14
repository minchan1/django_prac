# https://www.acmicpc.net/problem/1475

n = str(input())
list = [int(i) for i in n]
tmp = []
for num in list:
    if num == 6 or num ==9:
        k = (list.count(6)+list.count(9))/2
        tmp.append(k)
    else:
        tmp.append(list.count(num))
if int(max(tmp)) == max(tmp):
    print(int(max(tmp)))
else:
    print(int(max(tmp)+1))

# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    Fibo = [0,1]
    if n == 0 :
        return 0
    for i in range(n-1):
        Fibo.append(Fibo[-1]+Fibo[-2])
    return Fibo[-1]%1234567