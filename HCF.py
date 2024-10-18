def HCF(x, y):
    if x > y:
        min = y
    else:
        min = x
    for i in range(1, min+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
a= int(input("Enter 1st Number: "))
b= int(input("Enter 2nd Number: "))
Result=HCF(a,b)
print("HCF is: ",Result)