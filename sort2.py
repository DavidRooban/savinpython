list=[]
n=int(input("enter n-limit:"))
if(n>10000):
    print("enter less than 10000")
else:
    for i in range(1,n+1):
        a=(input("enter element :"))
        list.append(a)
        list.sort()
print '\n'.join([ str(a) for a in list ])
