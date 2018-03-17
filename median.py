list=[]
n=int(input("enter n-limit"))
if(n>1000):
    print("enter less than 1000")
else:
    for i in range(1,n+1):
        a=(input("enter element"))
        list.append(a)
        list.sort()
    if(n%2>0):
        print(list[(n//2)])
    else:
        print("greater median is")
        print(list[(n//2)])
