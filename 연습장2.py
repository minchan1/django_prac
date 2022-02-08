
n = int(input())
points = []
for _ in range(n):
    a,b = map(int,input().split())
    points.append([a,b])
ans = sorted(points, key = lambda x: (x[0],x[1]))
for i in range(n):    
    print(ans[i][0],ans[i][1])