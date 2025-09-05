"""n=int(input("enter a number:"))
if n==1:
    print("one")
elif n==2:
    print("Two")
elif n==3:
    print("Three")
elif n==4:
    print("four")
elif n==5:
    print("five")
else:
    print("invalid")

n=int(input("enter no of sub:"))
n1=int(input("enter sub1 marks:"))
n2=int(input("enter sub2 marks:"))
n3=int(input("enter sub3 marks:"))
n4=int(input("enter sub4 marks:"))
n5=int(input("enter sub5 marks:"))
avg=n1+n2+n3+n4+n5/5
if avg>=90:
    print("Grade-A")
elif avg>=80:
    print("Grade-B")
elif avg>=70:
    print("Grade-c")
elif avg>=60:
    print("Grade-d")
else:
    print("Fail")""" #or

T,H,E,M,S=map(int,input().split())
marks=(T+H+E+M+S)/5
if marks>=90:
    print(f"marks:{marks}->Grade:A")
elif marks>=80:
     print(f"marks:{marks}->Grade:B")
elif marks>=70:
     print(f"marks:{marks}->Grade:C")
elif marks>=60:
     print(f"marks:{marks}->Grade:D")
elif marks>=50:
     print(f"marks:{marks}->Grade:E")
else:
    print("fail")
