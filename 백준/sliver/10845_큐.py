from collections import deque

q = deque()

N = int(input())
for _ in range(N):
    word = input().split()


    if word[0] == 'push':
        q.append(int(word[1]))
    elif word[0] == 'pop':
        if q:
            w = q.popleft()
            print(w)
        else:
            print('-1')  
    elif word[0] == 'size':
        print(len(q))
    elif word[0] == 'empty':
        if q:
            print('0')
        else:
            print('1')
    elif word[0] == 'front':
        if q:
            print(q[0])
        else:
            print('-1')
    elif word[0] == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')


        
