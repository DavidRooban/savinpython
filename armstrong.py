num=int(input("enter a number"))
if(num>100000):
    print("enter less than 100000")
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print("yes")
else:
   print("no")
