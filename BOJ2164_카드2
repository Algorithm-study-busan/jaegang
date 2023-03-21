from collections import deque

n = int(input())
deque = deque([i+1 for i in range(n)])

while(len(deque) > 1):
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)
print(deque[0])