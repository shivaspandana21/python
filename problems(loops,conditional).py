n=int(input("enter a num:"))
while n>=10:
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n//=10
    n=sum
print(n)


n = int(input("Enter how many terms: "))
a, b = 0, 1   # first two terms
count = 0

print("Fibonacci series:")

while count < n:
    print(a, end=" ")   # print the current term
    c = a + b           # next term = sum of previous two
    a = b               # shift a to next
    b = c               # shift b to next
    count += 1


n=input("enter a string:")
reverse=""#empty string to bulid reverse
for character in n:#loop through each character
    reverse=character+reverse  #put current character first
print(reverse)  #prints reverse


s="python" # reverse a number with slicing
print(s[::-1])

s = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)



