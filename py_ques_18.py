# Ques 18 Using recursion write the python script for
# (a) printing binary numbers for a decimal numbers

def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:   
        return decimal_to_binary(n // 2) + str(n % 2)

num = int(input("Enter a decimal number: "))

print(f"Binary representation of {num} is: {decimal_to_binary(num)}")


# Ques 18 (b) printing octal numbers for a given decimal number
def decimal_to_octal(n):
    if n == 0:
        return ""
    return decimal_to_octal(n // 8) + str(n % 8)

num = int(input("Enter a decimal number: "))
octal_representation = decimal_to_octal(num) if num > 0 else "0"
print(f"Octal representation of {num} is: {octal_representation}")


# Ques 18 (c) printing factorial of a number
def factorial_num(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_num(n-1)

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial_num(n)}")


# Ques 18 (d) printing first n terms of fibonacci series
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci(n - 1)
        series.append(series[-1] + series[-2])
        return series

n = int(input("Enter the number of terms: "))
print(f"First {n} terms of Fibonacci series: {fibonacci(n)}")


# Ques 18 (e) calculate geometric sum upto n terms
def geometric_sum(n):
    if n == 0:
        return 1  
    return 1 / (2 ** n) + geometric_sum(n - 1)

n = int(input("Enter the number of terms: "))
print(f"Geometric sum up to {n} terms is: {geometric_sum(n):.5f}")


