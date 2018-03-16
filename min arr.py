list=[]
n=int(input("enter n-limit"))
if(n>100000):
    print("enter less than 100000")
else:
    for i in range(1,n+1):
        a=(input("enter element"))
        list.append(a)
    print(min(list))
