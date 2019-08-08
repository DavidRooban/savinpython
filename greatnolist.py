inp=int(input())
arr=list(map(int,input().split()))[:inp]
arr.sort(reverse=True)
if((sum(arr))==0):
    print("0")
else:
    print("".join(str(x) for x in arr))
