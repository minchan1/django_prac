# a = 5.0
# print(10*a)

# print(int(1.922))


# s = "1234"
# try:
#     int(s)
#     print(len(s))
# except:
#     print('False')


# participant = ["mislav", "stanko", "mislav", "ana","kaskd"]
# completion = ["stanko", "ana", "mislav"]

# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     return ''.join(i for i in participant)


# d = dict()
# for p in participant:
#     d[p] = d.get(p,0)+1
# for c in completion:
#     d[c] -= 1
# print(list(i for i, j in d.items() if j == 1))
# print(d.items)

# a = {}
# for i in range(len(participant)):a[i]=participant[i]
# for i in range(len(participant)):
#     if participant[i] in completion:
#         del a[i]
# print(a.values())

# s = "1 2 3 4"
# s = s.split(' ')
# for i in range(len(s)):
#     s[i] = int(s[i])
# a = f'{min(s)} {max(s)}'
# print(a)

# numbers = [3, 30, 34, 5, 9]
# nums = []
# answer = []
# for i in numbers:
#     if i >= 100 :
#         nums.append(i//100)
#     elif i < 100 and i >= 10:
#         nums.append(i//10)
#     elif i < 10:
#         nums.append(i)
# answer.append(max(nums))
# nums.remove(max(nums))

# print(answer)


def d(n):
    li = list(str(n))
    for i in li:
        n += int(i)
    print(n)
    
for i in range(1,10):
    d(i)