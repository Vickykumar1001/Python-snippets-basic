space=5
star=1
for i in range(0,9):
    if(i<4):
        for j in range(0,space):
            print("  ",end="")
        for k in range(0,star):
            print("* ",end="")
        space-=1
        star+=2
    else:
        for j in range(0,space):
            print("  ",end="")
        for k in range(0,star):
            print("* ",end="")
        space+=1
        star-=2
    print()