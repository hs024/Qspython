# for i in range(5):
#     for j in range(5,i,-1):
#         print("*",end="")
#     print()
n=5
for i in range(n):
    for j in range(2*n):
        if j>=n:
            if 2*n-j<=i:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            if j<i:
                print("*",end="")
            else:
                print(" ",end="")

    print()
