n=int(input("enter a number"))
a=1
if(n>0):
    for i in range(1,n+1):
        a=a*i
    print(a)
else:
    print("negative input")
