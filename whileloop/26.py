a="Hai Hello".split()
op={}
i=0
while i<len(a):
    value=[a[i],2*len(a[i]),a[i][::-1]+str(len(a[i]))]
    op[a[i]]=value
    i+=1
    
print(op)