import statistics
n=int(input())
a = list(map(int,input().split()))[:n]
a.sort()
print(statistics.median(a))
