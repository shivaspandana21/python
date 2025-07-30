n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
operator=input("enter operator(+,-,*,/):")

if operator=="+":
    print(f"addition of two numbers is :{n1+n2}")
elif operator=="-":
    print(f"subtraction of two numbers is :{n1-n2}")
elif operator=="*":
    print(f"multiplication of two numbers is :{n1*n2}")
elif operator=="/":
    print(f"division of two numbers is :{n1/n2}")
else:
    print("please enter vaild operator!")