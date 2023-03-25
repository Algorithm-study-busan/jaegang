m,n = map(int,input().split())
lst = [True]*(n+1)
lst[0],lst[1] = False, False
n_list = [i for i in range(2,int(n**0.5+1)+1)]
for i in n_list:
    if lst[i]:
        for j in range(i*2,n+1,i):
            lst[j] = False
for i in range(m,n+1):
    if lst[i]:
        print(i)