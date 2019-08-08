inp=int(input())
arr = list(map(int,input().split()))[:inp]
arr.sort()
print(*arr)
