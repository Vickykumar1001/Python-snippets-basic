s=input("Enter string: ")
new_s=""
for c in s:
    if c not in new_s:
        new_s+=c
print(new_s)
