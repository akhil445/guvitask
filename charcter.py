st1,st2=map(str,input().split())
a=0
for h in range(len(st1)):
  if st1[h]!=st2[h]:
    a=a+1
if(a==1):
  print("yes")
else:
  print("no")
