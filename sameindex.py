app=[]
inp=int(input())
arr=list(map(int,input().split()))[:inp]
for i in range(inp): 
  if arr[i] is i: 
    app.append(i)
app.sort()
print(*app)
