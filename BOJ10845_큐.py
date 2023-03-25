import sys
input = sys.stdin.readline
n = int(input())
queue = []
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        x = 1 if len(queue)==0 else 0
        print(x)
    elif command[0] == "back":
        x = queue[-1] if len(queue)!=0 else -1
        print(x)
    elif command[0] == "front":
        x = queue[0] if len(queue)!=0 else -1
        print(x)