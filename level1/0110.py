# https://programmers.co.kr/learn/courses/30/lessons/12940
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 최대공약수 : 두 수의 공통된 약수 중에서 가장 큰 수
# 최소공배수 : 두 수의 공통된 배수 중에서 가장 작은 수

def solution(n, m):
    a=m if m>n else n
    b=n if m>n else m
    ys1 = [i for i in range(1,a+1) if b%i == 0 and a%i ==0]
    bs1 = [b*i for i in range(1,a+1) for j in range(1,b+1) if b*i == a*j]
    return [max(ys1),min(bs1)]



# 과정 

n,m = 24,12
a=m if m>n else n
b=n if m>n else m
ys1 = []
for i in range(1,a+1):
    if b%i == 0 and a%i ==0: ys1.append(i) 
print(max(ys1))

bs1 = []
for i in range(1,a+1):
    for j in range(1,b+1):
        if b*i == a*j: bs1.append(b*i)
print(min(bs1))