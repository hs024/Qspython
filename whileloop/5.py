# wap to reverse of number
# a=187
# b=0
# while a>0:
#     r=a%10
#     a=a//10
#     b=b*10+r 
# print(b)
a=187 
b=0
while a>0:
    b=b*10+(a%10)
    a//=10
print(b)


