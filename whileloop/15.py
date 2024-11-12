# wap hi
# split fn 
# spli is a fn whic is Used to convert a str into  a list 
a="python is very easy"
# op={}
# i=0
# s=""
# while i<len(a):
#     if a[i]==" ":
#         op[s]=s[::-1]
#         s=""
#     s+=a[i]
#     i+=1
# op[s]=s[::-1]
# print(op)


b=a.split()
i=0
op={}
while i<len(b):
    op[b[i]]=b[i][::-1]
    i+=1
print(op)