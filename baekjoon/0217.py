# https://www.acmicpc.net/problem/4796

n=0
while True:
    n+=1
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:  # 0,0,0이 입력되면 break
        break
    if c%b<=a:  # 나머지가 a이하이면 
        ans = a*(c//b)+c%b
    else:       # 나머지가 a보다 커지면 a일 만큼만 캠핑가능
        ans = a*(c//b)+a
    print(f'Case {n}: {ans}') 