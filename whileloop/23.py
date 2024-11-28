#  wap to check a number perfect or not 
# 6 factor 1 2 3  sum is 6
a=6

i=1
s=0

while i<a:
    if a%i==0:
        s+=i
    i+=1
if s==a:
    print("perfect")
else:
    print("no")


