# wap extract all the vowels from a str with count
s="aeghiggobbbubbdhajjj"
c=0
i=0
o=""
v="aeiouAEIOU"
while i<len(s):
    if s[i] in v:
        o+=s[i]
        c+=1
    i+=1
print(o,c)
