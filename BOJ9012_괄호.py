import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    word = input()
    lst = []
    
    for x in word:
        if x == "[" or x == "(":
            lst.append(x)
        elif x == "]":
            if len(lst)!=0 and lst[-1]=='[':
                del lst[-1]
            else:
                lst.append(x)
                break
        elif x == ")":
            if len(lst)!=0 and lst[-1]=="(":
                del lst[-1]
            else:
                lst.append(x)
                break
    if lst == []:
        print("YES")
    else:
        print("NO")