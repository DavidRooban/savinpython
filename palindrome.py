def reverse(s):
    return s[::-1]
 
def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False
s=str(input())
ans = isPalindrome(s)
if(int(s)>10000):
    print("enter less than 10000")
elif ans == 1:
    print("yes")
else:
  print("no")
