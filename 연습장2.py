from collections import deque
s = "(())()"
s = deque(s)
if s.count('(') != s.count(')'):
    print('False')
elif s[0]==')' or s[-1]=='(':
    print('False')
else:
    while s:
        if s[0]==')':
            print('False')
            break   
        s.popleft()
        s.remove(')')
    print('True')