# FIND SECOND SMALLEST AND SECOND LARGEST

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
arr.sort()

print("second largest element: ",arr[-2])
print("second smallest element: ",arr[1])
