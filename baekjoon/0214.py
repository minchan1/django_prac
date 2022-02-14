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