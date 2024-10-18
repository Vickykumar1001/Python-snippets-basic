def LCM(x, y):
   if x > y:
       max = x
   else:
       max = y
   while(True):
       if((max % x == 0) and (max % y == 0)):
           lcm = max
           break
       max += 1
   return lcm

a= int(input("Enter 1st Number: "))
b= int(input("Enter 2nd Number: "))
Result=LCM(a,b)
print("LCM is: ",Result)