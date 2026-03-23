# COUNT FREQUENCY OF EACH CHARACTER IN STRING

s = input("enter string value: ")
dict1 = {}
for i in s:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print("frequency of each character is: ")
for i in dict1.items():
    print(i)
