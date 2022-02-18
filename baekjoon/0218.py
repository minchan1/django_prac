# https://www.acmicpc.net/problem/2822

tmp = []
for _ in range(8):
    tmp.append(int(input())) # 모든 점수를 저장
tmp2 = sorted(tmp,reverse=True)
ans = []
for i in range(5):
    ans.append(tmp.index(tmp2[i])+1)
    # 가장 큰 수 5개의 인덱스를 알아냄
ans.sort()

print(sum(tmp2[0:5]))
for num in ans:
    print(num,end=' ')