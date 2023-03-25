m1,n = map(int,input().split())
for m in range(m1,n+1): 
    if m==1:
        continue
    for i in range(2,int(m**0.5+1)):
        if m%i == 0:
            m+=1
            break
    else:
        print(m)
        m+=1