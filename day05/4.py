# wap to  check char is uppercase lower specialor a number

a=(input("enter:"))
if "A"<=a<="Z":
    print("upper")
elif "a"<=a<="z":
    print("lower")
elif "0"<=a<="9":
    print("number")
elif a in "!@#$%^&*()_+><,.';|][}{]":
    print("you are the special")
else:
    print("kahi or ka hai tu ")