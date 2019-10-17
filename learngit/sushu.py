def prime(m):
    k = 0
    for i in range(2,m):
        if m%i == 0:
            k = 0
            break
        else:
            k = 1
    if k==1:
        return 1
    else:
        return 0

n = eval(input())
ls = []
for i in range(1,n+1):
    if prime(i)==1:
        ls.append(i)

print(ls)
