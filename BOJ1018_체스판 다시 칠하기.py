n,m = map(int,input().split())
color = []

for i in range(n):
    color.append(input())

def chess2(color,a,b):
    cnt = 0
    temp = []
    for i in range(a,a+8):
        for j in range(b,b+8):
            temp.append(color[i][j])
    for i in range(0,64):
        if i%8==0 and i!=0 and temp[i] != temp[i-1]:
                temp[i] = 'W' if temp[i-1]=='W' else 'B'
                cnt+=1
        elif i%8 != 0:
            if temp[i] == temp[i-1]:
                temp[i] = 'W' if temp[i-1]=='B' else 'B'
                cnt+=1
    return cnt

def chess3(color,a,b):
    cnt = 1
    temp = []
    for i in range(a,a+8):
        for j in range(b,b+8):
            temp.append(color[i][j])
    
    temp[0] = 'W' if temp[0] =='B' else 'B'        
            
    for i in range(0,64):
        if i%8==0 and i!=0 and temp[i] != temp[i-1]:
            temp[i] = 'W' if temp[i-1]=='W' else 'B'
            cnt+=1
        elif i%8 != 0:
            if temp[i] == temp[i-1]:
                temp[i] = 'W' if temp[i-1]=='B' else 'B'
                cnt+=1
    return cnt

cnt = chess2(color,0,0)
for i in range(n-7):
    for j in range(m-7):
        if chess2(color,i,j) < cnt:
            cnt = chess2(color,i,j)
        if chess3(color,i,j) < cnt:
            cnt =chess3(color,i,j)
            
print(cnt)