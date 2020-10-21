l = int(input("Linhas: "))
s = 36
a = [0]*20
for i in range(l):
    for j in range(1,s+1):
        print(" ",end="")
    a[i] = 1
    for k in range(i+1):
        print('%6d'%(a[k]),end="")
    for m in range(i,0,-1):
        a[m] += a[m-1]
    s -=3
    print()
