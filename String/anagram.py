# ANAGRAM CHECKING
s1 = input("enter first word: ")
s2 = input("enter second word: ")
if sorted(s1.lower()) == sorted(s2.lower()):
    print("anagram")
else:
    print("not anagram")
