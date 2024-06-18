# Calculate the Area of a Rectangle:
def area_rectange():
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    print(f'The Area of Rectangle is: {length * breadth}')
    
# area_rectange()

# Check if a Number is Even or Odd:
def even_odd(n):
    if n % 2 == 0:
        print("Even Number")
    elif n % 2 != 0:
        print("Odd Number")

even_odd(61)

# Reverse a String:
def reverse_str(string):
    return string[::-1]

print(reverse_str("Reverse"))

# Find the Factorial of a Number:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Check if a String is Palindrome or Not:
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))

# Generate Fibonacci Series up to n terms:
def fib(n):
    a, b = 0 , 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(150)
    

# Find the Largest Among Three Numbers:
def largest_of_three(a, b, c):
    return max(a, b, c)

print(largest_of_three(5, 10, 13))

# Calculate Simple Interest:
def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(calculate_interest(1000, 7, 3))

# Convert Celsius to Fahrenheit:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(21))

# Check Leap Year:
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2020))

## Programming Challenges:
# Find the Median of Three Numbers:
def median_of_three(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]

print(median_of_three(10, 5, 7))

# Count the Number of Words in a Sentence:
def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("Hello world, this is a test sentence."))


# Find the Longest Common Prefix in a List of Strings:
def longest_common_prefix(string):
    prefix = string[0]
    
    for s in string[1:]:    
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break
        
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))

