number = input()
if number<=20:
  fact = 1
  for i in range(1,number+1): 
    fact = fact * i       
  print(fact) 
else:
  print("enter less than 20")
