a=1200
b=1.5
c=a+b
print(type(a))
print(type(b))
print(type(c))

num_int=int(5.7)
num_float=float("3.14")
message=str(42)
is_true=bool(1)
is_false=bool(0)
print(num_int)
print(num_float)
print(message)
print(is_true)
print(is_false)


x='spandy'
y=2
result=x*y
print(result)
# This will repeat the string 'spandy' two times
# Output: spandyspandy


#string to integer conversion
num_str="20"
num=int(num_str)
print(num)


# integer to string conversion
i=10
s=str(i)
print(s)

# float to integer conversion
f=1.5
n=int(f)
print(n)

# integer to float conversion
a=10
b=float(a)
print(b)

# float to string conversion
f=1.5
s=str(f)
print(s)


# string to float conversion
s="1.5"
f=float(s)
print(f)

# string to boolean conversion
s="true"
b=bool(s)
print(b)

# boolean to string conversion
b=True
s=str(b)
print(s)

#boolean to integer conversion
b=False
i=int(b)
print(i)

# integer to boolean conversion
i=1
b=bool(i)
print(b)

# float to boolean conversion
f=0.0
b=bool(f)
print(b)

# boolean to float conversion
b=False
f=float(b)
print(f)

# string to list conversion
s="hi"
l=list(s)
print(l)

s="pandu"
l=list(s)
print(l)

# list to string conversion
l=['p','a','n','d','u']
s=''.join(l)
print(s)

# list to tuple conversion
l = [1, 2, 3]
t = tuple(l)
print(t)

# tuple to list conversion
t =(1, 2, 3)
l = list(t)
print(l)

# list to set conversion
l = [1, 2, 3, 2, 1]
s = set(l)
print(s)

# set to list conversion
s = {1, 2, 3}
l = list(s)
print(l)

# tuple to set conversion
t = (1, 2, 3)
s = set(t)
print(s)

# set to tuple conversion
s = {1, 2, 3}
t = tuple(s)
print(t)

# dictionary to list conversion
d = {'a': 1, 'b': 2}
l = list(d.items())
print(l)

# list to dictionary conversion
l = [('a', 1), ('b', 2)]
d = dict(l)
print(d)

# dictionary to string conversion
d = {'a': 1, 'b': 2}
s = str(d)
print(s)

# string to dictionary conversion
s = "{'a': 1, 'b': 2}"
d = eval(s)  # Using eval for demonstration; use with caution
print(d)
# dictionary to tuple conversion
d = {'a': 1, 'b': 2}
t = tuple(d.items())
print(t)
# tuple to dictionary conversion
t = (('a', 1), ('b', 2))
d = dict(t)
print(d)
# set to dictionary conversion
s = {('a', 1), ('b', 2)}
d = dict(s)
print(d)

s = {('b', 1), ('a', 2)}
d = dict(s)
print(d)

# dictionary to set conversion
d = {'a': 1, 'b': 2}
s = set(d.items())
print(s)

# set to dictionary conversion
s = {('a', 1), ('b', 2)}
d = dict(s)
print(d)

# dictionary to boolean conversion
d = {'a': 1, 'b': 2} #d is non-empty anything other than empty dictionary is True
b = bool(d)
print(b)

d = {'a': 0, 'b': 0}# the dictionary is non empty,even through all values are 0,in python only empty containers(like{}) are false.the value inside doesnt matter for the boolean of the container.
b = bool(d)
print(b)

d = {} #d is empty dictionary
b = bool(d)
print(b)

# boolean to dictionary conversion
b = True
d = {'hi': b }  # Using a simple hi(we can use any word)-value pair
print(d)
d = {b: 'hi'}  # Using boolean as key
print(d)

b = False
d = {'hi': b}  # Using a simple hi(we can use any word)-value pair
print(d)
d = {b: 'hi'}  # Using boolean as key
print(d)

# boolean to set conversion
b = True
s = {b}  # Using a set with a single boolean value
print(s)

b = False
s = {b}# Using a set with a single boolean value
print(s)

# set to boolean conversion
s = {1, 2, 3}  # Non-empty set
b = bool(s)  # Non-empty set is True
print(b)

s={}
b=bool(s)
print(b)
# Empty set is False
s = set()  # Empty set
b = bool(s)  # Empty set is False
print(b)  
# set to string conversion
s = {1, 2, 3}
str_s = str(s)  # Converts set to string representation
print(str_s)

# string to set conversion
str_s = "{1, 2, 3}"
s= eval(str_s)  # Using eval for demonstration; use with caution
print(s)  # Converts string representation back to set

# set to integer conversion
s = {1, 2, 3}
i = len(s)  # Using length of set as integer representation
print(i)  # Output: 3

# integer to set conversion
i = 3
s = set(range(i))  # Creates a set with integers from 0 to i-1
print(s)  # Output: {0, 1, 2}

# integer to boolean conversion
i = 1
b = bool(i)  # Non-zero integer is True
print(b)  # Output: True


# boolean to integer conversion
b = True
i = int(b)  # True converts to 1
print(i)  # Output: 1 


