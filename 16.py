s,g=map(int,input().split())
for v in range(s,g):
   if v>1:
      for i in range(2,v):
        if(v%i)==0:
          break
      else:
          print(v,end=" ")
