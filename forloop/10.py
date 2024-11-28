a="abcada"

# op=""
# h={}
# for i in range(len(a)):
#     if a[i] in h:
#         op+=a[i]+h[a[i]]
#     else:
#         h[a[i]]=str(i+1)
#         op+=a[i]+h[a[i]]

op=""
for i in a:
    op+=i+str(ord(i)-96)
print(op)