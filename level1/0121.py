# https://programmers.co.kr/learn/courses/30/lessons/12935
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

def solution(arr):
    del arr[arr.index(min(arr))]
    if len(arr) == 0:
        arr.append(-1)
    return arr


# https://programmers.co.kr/learn/courses/30/lessons/42748
# 설명 생략

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
            array_i = array[commands[i][0]-1:commands[i][1]]
            array_i = sorted(array_i)
            answer.append(array_i[commands[i][2]-1])
    return answer
    # 더 줄여보기

# https://programmers.co.kr/learn/courses/30/lessons/42576
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
# 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p,0)+1
    for c in completion:
        d[c] -= 1
    return list(i for i, j in d.items() if j == 1).pop()