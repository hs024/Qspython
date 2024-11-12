# wap using count fn 
# to count the 
# count is a function which is used to calculate the substr present in a str  
# var.count(element)

i=0
s="ababaacbc"
op={}
while i<len(s):
    if s[i] not in op:
        c=s.count(s[i])
        op[s[i]]=c 
    i+=1
print(op)