# by me for only me 

import time 
a=input("enter")
s=" "
i=0
n=len(a)
for x in a:
    j=64
    while s[-1]!=x:
        time.sleep(0.02)
        print(s)
        s=s[:-1]+chr(j)
        j+=1
    s+=" "
print(s)