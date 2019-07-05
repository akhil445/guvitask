c=int(input())
if c>1:
  for i in range(2,c):
    if (c%i==0):
      print('no')
      break
  else:
    print('yes')     
else:
  print('no')
