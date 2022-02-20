# https://www.acmicpc.net/problem/1076

colors = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
c1 = str(input())
c2 = str(input())
c3 = str(input())
ans = str(colors.index(c1)) + str(colors.index(c2))
ans = int(ans)*(10**colors.index(c3))
print(ans)