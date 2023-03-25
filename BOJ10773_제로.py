from collections import deque
from sys import stdin

input = stdin.readline
k = int(input())
k_list = deque([])
for _ in range(k):
    t = int(input())
    if t==0:
        k_list.pop()
    elif t!=0:
        k_list.append(t)
        
print(sum(k_list))