# wap  to extract captital from even
i=0
s="aAdfAGHJIdfgg"
a=""
while i<len(s):
    if i%2==0 and "A"<=s[i]<="Z":
        a+=s[i]
    i+=1
print(a)
