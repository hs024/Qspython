# wap to extract vowels at even index  
a="aweipoyuU"
op=""
i=0
while i<len(a):
    if i%2==0 and a[i] in "aeiouAEIOU":
        op+=a[i]
    i+=1
print(op) 