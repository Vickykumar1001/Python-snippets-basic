def count_letters(S):
    count = {}
    for char in S: 
        if char in count: 
            count[char] += 1
        else: 
             count[char] = 1
    return count

S=input("Enter the String: ")
dictionary=count_letters(S)
print(dictionary)
