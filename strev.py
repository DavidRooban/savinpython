def rev(st): 
    st = st[::-1] 
    return st
s=raw_input()
if len(s)>10000:
  print("enter lesser lengthed string")
print(rev(s))
