# STRING PALINDROME
s = input("enter a string value: ")
rev = s[::-1]
print("given: ",s)
print("reversed: ",rev)
if s == rev:
    print("palindrome string")
else:
    print("not palindrome")
