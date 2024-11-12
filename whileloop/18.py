# wap to extract all str in a given list whose length more than 3
l=["asvfg","2jjff",6574,990,67.55,"a","b",55,"abc"]
ans=[]
i=0
while i<len(l):
    if type(l[i])==str and len(l[i])>3:
        ans.append(l[i])
    i+=1
print(ans)
