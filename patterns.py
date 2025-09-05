"""n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()
n=5
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print("*",end=" ")
    print()

n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(rows,end=" ")
    print()
n=5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()
n=5
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-rows+1,end=" ")
    print()
n=5
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-cols+1,end=" ")
    print() 
n=5
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print( )
for i in range(1,6):#rows
    for j in range(1,6):#columns
        print(j,end=" ")
    print( )

for i in range(1,4):#rows
    for j in range(1,9):#columns
        print("*",end=" ")
    print( )

for i in range(1,6):#rows
    for j in range(1,6):#columns
        print("*",end=" ")
    print( )

for i in range(1,4):#rows
    for j in range(1,9):#columns
        print("abc",end=" ")
    print( )
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):
    for j in range(1,6-i+1):
        print("*",end=" ")
    print()

count=0
a="pqrstuvwxyzabcd"
for i in range(1,6):
    for j in range(0,i):
        print(a[count],end=" ")
        count+=1
    print()


a="hello"
for i in range(1,6):
    for j in range(0,i):
        print(a[j],end=" ")
        
    print()
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,6):
    for s in range(5-i+1):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    print()
for i in range(1,6):
    for j in range(i*2+1):
        if  i==5 or :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""
# Hollow pyramid star pattern
for i in range(1, 6):
    for j in range(1, 2 * 5):
        # print star at boundary positions
        if j == 5 - i + 1 or j == 5 + i - 1 or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()