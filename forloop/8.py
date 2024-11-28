# wap to remove all the duplicate letter from a str
s="aabbccddabcd"

a=""
for i in s:
    if i not in a:
        a+=i

print(a)