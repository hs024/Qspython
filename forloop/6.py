# wap extract all capital letter present in str but at even index
s="ABCabcDE"
a=""
for i in range(len(s)):
    if i%2==0 and "A"<=s[i]<="Z":
        a+=s[i]
print(a)