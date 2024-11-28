s="HELLO HIE"
i=0
a=""
while i<len(s):
    if "A"<=s[i]<="Z":
        a+=chr(ord(s[i])+32)
    else:
        a+=s[i]
    i+=1
print(a)

