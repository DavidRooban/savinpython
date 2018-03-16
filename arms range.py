num=int(input("enter starting range"))
n=int(input("enter ending range"))
for i in range(num,n):
    if(i>100000):
        print("enter less than 100000")
    sum = 0
    temp = i
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    if i == sum:
       print(i)
