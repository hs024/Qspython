# wap to multivalue datatype
a=eval(input("enter:"))
s=[list,str,tuple,set,dict]

if type(a) in s:
    print("yes it mvdt ",a," ",type(a))
else:
    print("no")

