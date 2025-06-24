#arithmetic operators

#addition
a=10
b=20
c=a+b
print("Addition:", c) # This will add 10 and 20, resulting in 30
#subtraction
c=a-b
print("Subtraction:", c)    # This will subtract 20 from 10, resulting in -10
#multiplication
c=a*b
print("Multiplication:", c) # This will multiply 10 by 20, resulting in 200
#division   
c=a/b
print("Division:", c)   # This will perform floating-point division, resulting in 0.5
#floor division
c=a//b  
print("Floor Division:", c) # since 10 < 20, the result is 0
#modulus
c=a%b   
print("Modulus:", c) # since 10 < 20, the result is 10
#exponentiation
c=a**b
print("Exponentiation:", c) # This will raise 10 to the power of 20, which is a very large number

#assignment operators

#assigning value to a variable
a = 10
#assigning value to a variable using addition
a += 5
print("After += 5, a:", a)  # This will add 5 to 10, resulting in 15
a=10
b=20
a += b 
print("After += b, a:", a)  # This will add 20 to 10, resulting in 30
b += a
print("after += a, b:",b) # This will add 30 to 20, resulting in 50
a=100
b=200
a += b
print("after += b, a:",a) # This will add 200 to 100, resulting in 300

#assigning value to a variable using subtraction
a = 10  
a -= 5
print("After -= 5, a:", a)  # This will subtract 5 from 10, resulting in 5
a=10
b=20    
a -= b
print("After -= b, a:", a)  # This will subtract 20 from 10, resulting in -10
b -= a  
print("After -= a, b:", b)  # This will subtract -10 from 20, resulting in 30

#assigning value to a variable using multiplication
a = 10
a *= 5
print("After *= 5, a:", a)  # This will multiply 10 by 5, resulting in 50
a=10    
b=20
a *= b  
print("After *= b, a:", a)  # This will multiply 10 by 20, resulting in 200
b *= a
print("After *= a, b:", b)  # This will multiply 20 by 200, resulting in 4000

#assigning value to a variable using division
a = 10      
a /= 5
print("After /= 5, a:", a)  # This will divide 10 by 5, resulting in 2.0
a=10        
b=20
a /= b
print("After /= b, a:", a)  # This will divide 10 by 20, resulting in 0.5
b /= a
print("After /= a, b:", b)  # This will divide 20 by 0.5, resulting in 40.0

#assigning value to a variable using floor division
a = 10
a //= 5
print("After //= 5, a:", a)  # This will perform floor division of 10 by 5, resulting in 2
a=10    
b=20
a //= b
print("After //= b, a:", a)  # This will perform floor division of 10 by 20, resulting in 0
#b //= a
#print("After //= a, b:", b)  # This will perform floor division of 20 by 0, resulting in an error

#assigning value to a variable using modulus
a = 10
a %= 5
print("After %= 5, a:", a)  # This will perform modulus of 10 by 5, resulting in 0
a=10    
b=20
a %= b
print("After %= b, a:", a)  # This will perform modulus of 10 by 20, resulting in 10
b %= a
print("After %= a, b:", b)  # This will perform modulus of 20 by 10, resulting in 0

#assigning value to a variable using exponentiation
a = 10
a **= 2
print("After **= 2, a:", a)  # This will raise 10 to the power of 2, resulting in 100
a=10
b=20
a **= b
print("After **= b, a:", a)  # This will raise 10 to the power of 20, resulting in a very large number
b **= a
print("After **= a, b:", b)  # This will raise 20 to the power of a (which is a very large number), resulting in an extremely large number

