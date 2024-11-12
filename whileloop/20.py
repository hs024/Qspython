


# wap # wap 
em="HimAnshu123@gmail.com"

u=[]
l=[]
d=[]
s=[]
i=0
while i<len(em):
    if "A"<=em[i]<="Z":
        u.append(em[i])
    elif "a"<=em[i]<="z":
        l.append(em[i])
    elif "0"<=em[i]<="9":
        d.append(em[i])
    else:
        s.append(em[i])
    i+=1
print(u)
print(l)
print(d)
print(s)