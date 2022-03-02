# https://www.acmicpc.net/problem/1065

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

num = int(input())
n = 1
cnt = 0

# 한수인지 판별하는 함수
def hansu(n):
    if 1<=n<10:
        return True
    tmp = []
    for num in str(n):
        tmp.append(int(num))
    k = tmp[1] - tmp[0]
    # 각 자릿수의 차가 공차와 다르면 False
    for i in range(1,len(tmp)-1):
        if tmp[i+1] - tmp[i] != k:
            return False
    return True

# 함수의 결과값이 True인 경우만 카운트
while n<=num:
    if hansu(n):
        cnt+=1
    n+=1
print(cnt)