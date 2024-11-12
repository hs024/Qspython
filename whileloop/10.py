# wap extract all integer from a given list
l=[1,2,5.0,"a","j",4,"9","k"]
e=[]
i=0

while i<len(l):
    if type(l[i]) in [int,float]:
        e.append(l[i])
    i+=1
print(e)