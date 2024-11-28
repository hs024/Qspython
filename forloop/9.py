#  wap 
a="python is very easy".split()
op={}
for i in range(len(a)):
    if i%2==0:
        op[a[i]]=len(a[i])
    else:
        op[a[i]]=a[i][::-1]
print(op)