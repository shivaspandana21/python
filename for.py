#range(start,stop,step)
#range(0,n,1)
for i in range(6):#prints from 0 to 5 that means starts from 0 to n+1
    print(i)

for i in range(1,6):#prints from 1 to 5 that means starts from 1 to n+1
    print(i)
for i in range(6):#starts from 0 to n+1
    print(i,end=" ")#prints everthing in same line i.e,horizontal(rows)

for i in range(5,0,-1):#starts from n to 0,-1 in decreasing order
    print(i)
for i in range(5):#starts from 0 and prints till 4 (n+1)
    print(i,end=" ")#prints everthing in same line i.e,horizontal(rows)
print()
for j in range(1,6):#prints from 1 to 5 that means starts from 1 to n+1
    print(j,end=" ")
print()
for k in range(5,0,-1):#starts from n to 0,-1 in decreasing order
    print(k,end=" ")
print()


for i in range(0,31,2):#starts from 0,till 30,step 2
    print(i,end=" ")#prints everthing in same line i.e,horizontal(rows)

for i in range(31): #starts from 0 and end till 30
    if i&1==0:#checks it is even or not
        print(i,end=" ")
#reverse for strings
a=input()
rev=""
for character in a:
    rev=character+rev 
print(rev)

#reverse for numbers
a=int(input("enter a number:"))
rev,rem=0,0
while a!=0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)

#palindrome
a=int(input("enter a number:"))
rev,rem=0,0
b=a
while a!=0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
if rev==b:
    print("palindrome")
else:
    print("not palindrome")
#fibonocci series
n=int(input("enter n value:"))
first,next=0,1
#print(first,next,end=" ")
for i in range(0,n):
    sum=first+next
    #print(sum,end=" ")
    first=next
    next=sum
print(sum)

#factorial
n=int(input("enter a num:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
#sum of digits until the digit becomes single 
a=int(input("enter a number:"))
while a>=10:
    rem,sum=0,0
    while a!=0:
        rem=a%10
        sum=sum+rem
        a=a//10
    a=sum
print(a)

#prime number
n=int(input())
count=0
times=0
temp=0
for i in range(2,n):
    times+=1
    if n%i==0:
        temp=1
        break
print("times:",times)
if temp==0:
    print(f" {n} it is prime")
else:
    print(f" {n} it is not prime")

#sum of number
n=int(input("enter a num:"))
sum,rem=0,0
while n>0:
    rem=n%10
    sum=sum+rem
    n//=10
print(sum)