# wap special char in emal
e="him_1#$%hjdjhj44bb@gmail.com"
i=0
ext=""
sp=["@","#","$","%",".",";",":","*","+","_","/","?","^","&","-","`"]
while i<len(e):
    if e[i] in sp:
        ext+=e[i]
    i+=1
print(ext)