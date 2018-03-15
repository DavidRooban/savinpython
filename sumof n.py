n=int(input("Enter the number:"))
if(n<0):
    print("wrong input")
else:
    for i in range(n):
        print(i+1)
    x=int(input("enter no.of digits to be added:"))
    sum=x*(x+1)/2
    print (sum)
