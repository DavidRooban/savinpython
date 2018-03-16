num = int(input("Enter starting range: "))
n=int(input("enter ending limit"))
if(num>10000 or n>10000):
    print("enter less than 10000")
else:
   for i in range(num+1,n):
       if (i % 2) > 0:
           print(i)
