
a="(()))(())"


op1=0
op2=0
i=0


while i <len(a):
    if a[i]=="(":
        op1+=1
    else:
        op1-=1
    i+=1

print(abs(op1))
    
