
a="Python Programming while good"
op={}
l=a.split()

i=0
while i<len(l):
    op[l[i]]=l[i].count("h")
    # if l[i].count("h")>=1:
    #     op[l[i]]=1
    # else:
    #     op[l[i]]=0
    i+=1
print(op)