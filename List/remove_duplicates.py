# REMOVE DUPLICATE ELEMENTS FROM LIST

def lst():
    size = int(input("enter size of list: "))
    l = []
    for i in range(1,size+1):
        print("enter element",i,": ",end='')
        a = int(input())
        l.append(a)
    return(l)

arr = lst()
print("given list: ",arr)

temp = []
for i in arr:
    if i not in temp:
        temp.append(i)
print("updated list ( removed duplicate values: )\n",temp)
