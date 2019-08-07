num = int(input())
n=int(input())
if(num>100000 or n>100000):
    print("enter less than 100000")
else:
   for i in range(num+1,n):
       if (i % 2) > 0:
           print(i)
