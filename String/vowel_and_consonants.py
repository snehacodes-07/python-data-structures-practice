# COUNT VOWELS AND CONSONANTS
s = input("enter a string value: ")
vow = 0
cons = 0
for i in s:
    if i.isalpha():
           if i == "aeiou" or i == "AEIOU":
               vow+=1
           else:
               cons+=1
print("total vowels: ",vow)
print("total consonants: ",cons)
