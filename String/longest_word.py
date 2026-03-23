# LONGEST WORD IN A SENTENCE

s = input("enter a sentence: ")
abc = s.split(" ")
maxi = 0
word = ''
for i in abc:
    count = len(i)
    if count > maxi:
        maxi = count
        word = i
print("longest word: ",word)
print("no. of characters: ",maxi)
    
