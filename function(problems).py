def is_palindrome(word):
    word=word.lower()
    return word==word[::-1]
print(is_palindrome("Madam"))
print(is_palindrome("dog"))

def sum_even(numbers):
    total=0
    for n in numbers:
        if n%2==0:
            total=total+n
    return total
print(sum_even([1,2,3,4,5,6]))
