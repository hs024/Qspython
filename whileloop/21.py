# wap  take a list but behave  like set 
 
l=[1,2,3,4,5,6,1,3,4,5]


op=[]
i=0


while i<len(l):
    if l[i] not in op:
        op+=[l[i]]
    i+=1
print(op)
