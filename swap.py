x=input()
y=list(x)
y[::2],y[1::2]=y[1::2],y[::2]
''.join(y)
print(*y,sep="")
