# wap to extract all the integer from a list
s=[1,"f","4",6,"jjj",9]
o=[]
for i in s:
    if type(i)==int:
        o+=[i]
print(o)