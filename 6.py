L=[4,6,9,12,11,15,19]

for i in L:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        print(i)
        break