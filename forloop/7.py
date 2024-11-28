a=[10,"hello",3+5j,[1,2,3],9.8]
# op=[1,5,1,3,1]
# /single value multivalue datatype
op=[]
for i in a:
    if type(i) in [int,float,complex,bool]:
        op+=[1]
    else:
        op+=[len(i)]
print(op)