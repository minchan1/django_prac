# from collections import deque
progresses = [93, 30, 55]
speeds = [1, 30, 5]
remain = []
result = []
cnt = []
for i in range(len(progresses)):
    tmp=(100-progresses[i])/speeds[i]
    if int(tmp) == tmp:
        remain.append(int(tmp))
    else:
        remain.append(int(tmp)+1)
# remain = deque(remain)
for i in range(len(remain)):
    if result:
        if result[0]>=remain[i]:
            result.append(remain[i])
        else:
            cnt.append(len(result))
            result.clear()
            result.append(remain[i])
    else:
        result.append(remain[i])
if result:
    cnt.append(len(result))
print(cnt)