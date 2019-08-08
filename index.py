inp=int(input())
array=list(map(int,input().split()))[:inp]
for x in range(0,inp):
    print(array[x],x)
