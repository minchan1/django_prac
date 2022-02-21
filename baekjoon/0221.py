# https://www.acmicpc.net/problem/2947

blocks = list(map(int,(input().split())))
while blocks != [1,2,3,4,5]:
    for i in range(4):
        a,b=blocks[i],blocks[i+1]
        if a>b:
            blocks[i+1]=a
            blocks[i]=b
            for j in blocks:
                print(j,end=' ')
    print()