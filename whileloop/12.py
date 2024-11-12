# wap 
s="DAtaSCIEnCe"
c=0
i=0
op=""
while i<len(s):
    if "A"<=s[i]<="Z":
        op+=s[i]
        c+=1
    i+=1
op+=str(c)
print(op)