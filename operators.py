# comparision operators
#equals to(==)
a=10
b=20
c=a==b
print("equals to:",c)   # This will compare 10 and 20, resulting in False

a=10
b=10
c=a==b
print("equals to:",c) # This will compare 10 and 10, resulting in True

#not equals to(!=)
a=10
b=20
c=a!=b
print("not equals to:",c) # This will compare 10 and 20, resulting in True

a=10
b=10
c=a!=b
print("not equals to:",c)   

#greater than(>)
a=10
b=20
c=a>b
print("greater than:",c) # This will compare 10 and 20, resulting in False

a=30
b=20
c=a>b
print("greater than:",c) # This will compare 30 and 20, resulting in True

a=20
b=20
c=a>b
print("greater than:",c) # This will compare 20 and 20, resulting in False

#less than(<)
a=10
b=20
c=a<b
print("less than:",c) # This will compare 10 and 20, resulting in True

a=40
b=20
c=a<b
print("less than:",c) # This will compare 40 and 20, resulting in False

a=40
b=40
c=a<b
print("less than:",c) # This will compare 40 and 20, resulting in False 

#greater than or equal to(>=)
a=10
b=20    
c=a>=b
print("greater than or equal to:",c) # This will compare 10 and 20, resulting in False

a=30
b=20    
c=a>=b
print("greater than or equal to:",c)    # This will compare 30 and 20, resulting in True

a=10
b=10    
c=a>=b
print("greater than or equal to:",c) # This will compare 10 and 10, resulting in True

#less than or equal to(<=)
a=10
b=20
c=a<=b
print("less than or equal to:",c) # This will compare 10 and 20, resulting in True

a=100
b=20
c=a<=b
print("less than or equal to:",c)   # This will compare 100 and 20, resulting in False

a=100
b=100
c=a<=b
print("less than or equal to:",c) # This will compare 100 and 100, resulting in True

#logical operators
# and operator
a = True
b = False   
c = a and b
print("and operator:", c)  # This will return False because one of the operands is False 

a = True
b = True   
c = a and b
print("and operator:", c)   # This will return True because both operands are True

a = False
b = False   
c = a and b
print("and operator:", c)   # This will return False because both operands are False

# or operator
a = True
b = False
c = a or b
print("or operator:", c)  # This will return True because one of the operands is True

a = False
b = False   
c = a or b
print("or operator:", c) # This will return False because both operands are False

a = True
b = True    
c = a or b
print("or operator:", c)  # This will return True because both operands are True 

# not operator
a = True
b = not a
print("not operator:", b)  # This will return False because not True is False

a = False
b = not a   
print("not operator:", b)  # This will return True because not False is True

#membership operators
# in operator
my_list = [1, 2, 3, 4, 5]
a = 3
b = a in my_list
print("in operator:", b)  # This will return True because 3 is in the list 

my_list = [1, 2, 3, 4, 5]
a = 7
b = a in my_list
print("in operator:", b) # This will return False because 7 is not in the list 

fruits=['apple','banana','watermelon','mango']
a='mango'
b= a in fruits
print("in operator:",b) # This will return True because 'mango' is in the list

# not in operator
my_list = [1, 2, 3, 4, 5]   
a = 3
b = a not in my_list    
print("not in operator:", b)  # This will return False because 3 is in the list 

my_list = [1, 2, 3, 4, 5]
a = 7   
b = a not in my_list
print("not in operator:", b)  # This will return True because 7 is not

fruits=['apple','banana','watermelon','mango']
a='mango'
b= a  not in fruits
print(" not in operator:",b) # This will return False because 'mango' is in the list

#identity operators
# is operator
a = [1, 2, 3]
b = a
c = a is b
print("is operator:", c)  # This will return True because a and b refer to the same object

a = [1, 2, 3]
b = [1, 2, 3]       
c = a is b
print("is operator:", c)  # This will return False because a and b are different objects with the same content

a="spandy"
b="spandy"
c = a is b
print("is operator:", c)  # This will return True because a and b refer to the same string object in memory

a="spandy"
b="pandu"
c = a is b
print("is operator:", c) # This will return False because a and b refer to different string objects
 
# is not operator
a = [1, 2, 3]
b = [1, 2, 3]
c = a is not b
print("is not operator:", c)  # This will return True because a and b are different objects

a = [1, 2, 3]
b = a
c = a is not b
print("is not operator:", c)  # This will return False because a and b refer to the same object

a="spandy"
b="pandu"
c = a is not b
print("is operator:", c)    # This will return True because a and b refer to different string objects

a="spandy"
b="spandy"  
c = a is not b
print("is operator:", c)  # This will return False because a and b refer to the same string object in memory

# bitwise operators
# bitwise AND operator
a=2
b=3
c = a & b
print("bitwise AND operator:", c)  # This will return 2 because 2 in binary is 10 and 3 is 11, so the AND operation results in 10 (which is 2 in decimal)

a=5
b=10
c = a & b
print("bitwise AND operator:", c)  # This will return 0 because 5 in binary is 101 and 10 is 1010, so the AND operation results in 0000 (which is 0 in decimal)

a=6
b=3 
c = a & b
print("bitwise AND operator:", c)  # This will return 2 because 6 in binary is 110 and 3 is 011, so the AND operation results in 010 (which is 2 in decimal)

# bitwise OR operator
a=2
b=3
c = a | b   
print("bitwise OR operator:", c)  # This will return 3 because 2 in binary is 10 and 3 is 11, so the OR operation results in 11 (which is 3 in decimal)

a=5
b=10    
c = a | b
print("bitwise OR operator:", c)  # This will return 15 because 5 in binary is 101 and 10 is 1010, so the OR operation results in 1111 (which is 15 in decimal)

a=6
b=3         
c = a | b
print("bitwise OR operator:", c)  # This will return 7 because 6 in binary is 110 and 3 is 011, so the OR operation results in 111 (which is 7 in decimal)

# bitwise XOR operator
a=2 
b=3
c = a ^ b
print("bitwise XOR operator:", c)  # This will return 1 because 2 in binary is 10 and 3 is 11, so the XOR operation results in 01 (which is 1 in decimal)

a=5
b=10    
c = a ^ b
print("bitwise XOR operator:", c)  # This will return 15 because 5 in binary is 101 and 10 is 1010, so the XOR operation results in 1111 (which is 15 in decimal)

a=6
b=3
c = a ^ b
print("bitwise XOR operator:", c)  # This will return 5 because 6 in binary is 110 and 3 is 011, so the XOR operation results in 101 (which is 5 in decimal)

# bitwise NOT operator
a=2
b = ~a
print("bitwise NOT operator:", b)  # This will return -3 because the bitwise NOT operation flips all bits, so 2 in binary (10) becomes -3 in two's complement representation

a=5
b = ~a
print("bitwise NOT operator:", b)  # This will return -6 because the bitwise NOT operation flips all bits, so 5 in binary (101) becomes -6 in two's complement representation

a=6
b = ~a
print("bitwise NOT operator:", b)  # This will return -7 because the bitwise NOT operation flips all bits, so 6 in binary (110) becomes -7 in two's complement representation

# bitwise left shift operator
a=2
b = a << 1
print("bitwise left shift operator:", b)  # This will return 4 because left shifting 2 (10 in binary) by 1 bit results in 100 (which is 4 in decimal)

a=5
b = a << 2  
print("bitwise left shift operator:", b)  # This will return 20 because left shifting 5 (101 in binary) by 2 bits results in 10100 (which is 20 in decimal)

a=6
b = a << 3  
print("bitwise left shift operator:", b)  # This will return 48 because left shifting 6 (110 in binary) by 3 bits results in 110000 (which is 48 in decimal)

# bitwise right shift operator
a=2 
b = a >> 1
print("bitwise right shift operator:", b)  # This will return 1 because right shifting 2 (10 in binary) by 1 bit results in 1 (which is 1 in decimal)

a=32
b = a >> 2
print("bitwise right shift operator:", b)  # This will return 8 because right shifting 32 (100000 in binary) by 2 bits results in 1000 (which is 8 in decimal)

a=64
b = a >> 3
print("bitwise right shift operator:", b)  # This will return 8 because right shifting 64 (1000000 in binary) by 3 bits results in 1000 (which is 8 in decimal)

a=2004
b = a >> 2
print("bitwise right shift operator:", b)  # This will return 501 because right shifting 2004 (11111010100 in binary) by 2 bits results in 111110101 (which is 501 in decimal)
a=10
b=20
c=a==b
print("equals to:",c)