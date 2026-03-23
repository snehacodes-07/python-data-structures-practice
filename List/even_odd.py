# SEPARATE EVEN AND ODD ELEMENTS IN 2 DIFF LISTS

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

even = []
odd = []
for i in arr:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even list: ",even)
print("odd list: ",odd) 
