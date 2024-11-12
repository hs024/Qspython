# wap 
em="HimAnshu123@gmail.com"
h={"u":[],"l":[],"d":[],"s":[]}
i=0
while i<len(em):
    if "A"<=em[i]<="Z":
        h["u"].append(em[i])
    elif "a"<=em[i]<="z":
        h["l"].append(em[i])
    elif "0"<=em[i]<="9":
        h["d"].append(em[i])
    else:
        h["s"].append(em[i])
    i+=1
print(h["u"])
print(h["l"])
print(h["d"])
print(h["s"])




# # wap # wap 
# em="HimAnshu123@gmail.com"
# h={"u":[],"l":[],"d":[],"s":[]}
# u=[]
# l=[]
# d=[]
# s=[]
# i=0
# while i<len(em):
#     if "A"<=em[i]<="Z":
#         u.append(em[i])
#     elif "a"<=em[i]<="z":
#         l.append(em[i])
#     elif "0"<=em[i]<="9":
#         d.append(em[i])
#     else:
#         s.append(em[i])
#     i+=1
# print(u)
# print(l)
# print(d)
# print(s)