# FIRST LETTER OF EACH WORD IN UPPERCASE

s = input("enter string: ")
word = s.split()
for i in word:
    i = i.capitalize()
    print(i,end=" ")
