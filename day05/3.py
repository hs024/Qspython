# wap to  check nu is divisble 3 then print fizz  or by 5 buzz by both fizzbuzz

a=int(input("enter:"))

if a%3==0 and a%5==0:
    print("fizzbuzz")
elif a%3==0:
    print("fizz")
elif a%5==0:
    print("buzz")
else:
    print("dekh lenge")
