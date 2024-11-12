# wap to extract all uppercase of all string
# print(ord("Z"))
s="aDrGhhJ"
ext=""
i=0
while i<len(s):
    if s[i]>="A" and s[i]<="Z":
        ext+=s[i]
    i+=1
print(ext)