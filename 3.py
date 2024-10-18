s = "Computer Programming"

print("Given String:", s)
 
print("After replacing vowels with _: ",end=""),
vowels = 'AEIOUaeiou'
for ele in vowels:
    s = s.replace(ele, "_")
print(s)
