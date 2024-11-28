# wap extract uppercase
s="aAbChhD"
o=""
for i in s:
    if "A"<=i<="Z":
        o+=i

print(o)