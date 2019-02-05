def rev(numb): 
    numb = numb[::-1] 
    return numb
s=raw_input()
if len(s)>10000:
  print("enter lesser lengthed string")
print(rev(s))
