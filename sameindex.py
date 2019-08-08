app=[]
inp=int(input())
arr=list(map(int,input().split()))[:inp]
for i in range(inp): 
  if arr[i] is i: 
    app.append(i)
if (len(app)==0):
  print("-1")
else:
  app.sort()
  print(*app)
