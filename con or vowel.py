list=['a','e','i','o','u','A','E','I','O','U']
r=raw_input()
if(r in list):
    print"Vowel"
elif r.isalpha():
  print"Consonant"
else:
  print("invalid")
