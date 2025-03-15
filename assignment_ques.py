# #Ques-3 Write python script to print table of 5 upto users choice
# n = int(input("Enter the number upto which you want to print the table : "))
# for i in range(1 ,n+1):
#     print(f" 5 * {i} = {5*i}")


# #Ques-4 Write python script to find given number is even or odd
# n = int(input("Enter a number to find given number is even or odd : "))
# if(n%2==0):
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")

# #Ques-5 Write python script to find given number is leap year or not
# n = int(input("Enter a number to find given number is leap year or not : "))
# if((n%4==0 and n%100 != 0) or (n%400 == 0)):
#     print(f"{n} is leap year")
# else:
#     print(f"{n} is not a leap year")

# #Ques-6 Write a python script to find given number is prime or composite
# n = int(input("Enter a number : "))
# for i in range(2,n):
#     if(n%i == 0):
#         print(f"{n} is a composite number")
#         break
# else:
#     print(f"{n} is prime number")

# #Ques-7 Write python script to find sum of first n natural numbers
# n = int(input("Enter a number : "))
# sum=0
# for i in range(1, n+1):
#     sum = sum + i
# print("Sum is : ", sum)

# #Ques-8 Write python script to find factorial of a given number
# n = int(input("Enter a number : "))
# fact=1
# for i in range(1, n+1):
#     fact = fact * i
# print("Factorial is : ", fact)

# #Ques-9 Write a python script to find sum of digits of a given number
# n = int(input("Enter a number : "))
# sum = 0 
# digit = 0
# while n != 0 :
#     digit = n%10
#     sum = sum + digit
#     n = n // 10
# print("Sum of digits is ", sum)

# #Ques-10 Write python script to find reverse of a given number
# n = input("Enter a number : ")
# reverse = n[: : -1]
# print(reverse)

# #Ques- 11 Write a python script to find whether given number is palindrome or not
# n = input("Enter a number")
# reverse = n[: : -1]
# if(n==reverse):
#     print(f"{n} is palindrome")
# else:
#     print(f"{n} is not a palindrome")

# #Ques-12 Write a python script to print fibonacci series upto n terms
# n = int(input("Enter a number : "))
# count = 0 
# a = 0 
# b = 1
# print(a)
# print(b)
# fib = 0
# while( n >= count):
#     fib = a + b
#     print(fib)
#     a = b
#     b = fib
#     count = count + 1

# #Ques - 13  Write a python scriptto print 100 even numbers
# count = 0
# num = 2
# while(count < 100):
#     print(num)
#     num = num + 2
#     count = count + 1

# #Ques - 14 Write a python script to find whether a given number is armstrong number or not
# n = int(input("Enter a number : "))
# original_num = n
# sum=0
# digit = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit**3
#     n = n // 10
# if(original_num == sum):
#     print(f"{original_num} is an armstrong number")
# else:
#     print(f"{original_num} is not an armstrong number")

# #Ques- 15 Write a python script to print all palindromes for a range 500-1000
# for i in range(500,1000):
#     i = str(i)
#     reverse = i[::-1]
#     if(reverse == i):
#         print(i,end=" ")

# # Ques- 16-(a) Print following patterns
# # *
# # **
# # ***
# # ****
# n = int(input("Enter a number upto which row you want to print the pattern : "))
# i = 0
# while (i < n):
#     j = 0
#     while ( j <= i):
#         print("*", end=" ")
#         j = j + 1
#     print("\n")    
#     i=i+1

# # Ques 16(b)
# # ****
# # ***
# # **
# # *
# n = int(input("Enter a number upto which row you want to print the pattern : "))
# i = 1
# while (i <= n):
#     j = n
#     while ( j >= i):
#         print("*", end=" ")
#         j = j - 1
#     print("\n")    
#     i=i+1

# # Ques 16 (c)
# #     *
# #   * * *
# #  * * * * *
# n =  int(input("Enter a number upto which row you want to print the pattern : "))
# i = 0
# while( i < n):
#     j = n - i
#     while( j > 0 ):
#         print( " " , end = " ")
#         j = j - 1
#     # print("\n")
    
#     j = 0
#     while( j <= i):
#         print("*" , end = " ")
#         j = j + 1

#     j = 1
#     while(j <= i):
#         print("*" , end = " ")
#         j = j + 1
#     print("\n")
#     i = i + 1

# # Ques 16 (d)
# # 1
# # 22
# # 333
# # 4444
# n =  int(input("Enter a number upto which row you want to print the pattern : "))
# i = 1
# while(i <= n):
#     j = 1
#     while( j <= i):
#         print(i , end=" ")
#         j = j + 1
#     print("\n")
#     i = i + 1

# # Ques 16 (f)
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
# n = int(input("Enter a number upto that row you want to print floyds triangle : "))
# i = 0
# count = 1
# while( i < n):
#     j = 0
#     while( j <= i):
#         print(count , end=" ")
#         count = count + 1
#         j = j + 1
#     print("\n")
#     i = i + 1

# # Ques 17 Using functions write python script for
# # (a) finding whether a given number is palindrome or not

# def is_palindrome( n ):
#     original_n = n
#     reverse = n[ : : -1]
#     if(reverse == original_n):
#         print(f"{original_n} is Palindrome number")
#     else:
#         print(f"{original_n} is not a palindrome number")

# n = input("Enter a number : ")
# is_palindrome(n)

# # Ques 17 (b) finding sum of first n natural numbers
# def sum_natural_numbers(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#     return sum

# n = int(input(" Enter a number : "))
# print(f"Sum of first {n} natural numbers is {sum_natural_numbers(n)}")

# # Ques 18 Using recursion write the python script for
# # (a) printing binary numbers for a decimal numbers

# def decimal_to_binary(n):
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:   
#         return decimal_to_binary(n // 2) + str(n % 2)

# num = int(input("Enter a decimal number: "))

# print(f"Binary representation of {num} is: {decimal_to_binary(num)}")

# # Ques 18 (b) printing octal numbers for a given decimal number
# def decimal_to_octal(n):
#     if n == 0:
#         return ""
#     return decimal_to_octal(n // 8) + str(n % 8)

# num = int(input("Enter a decimal number: "))
# octal_representation = decimal_to_octal(num) if num > 0 else "0"
# print(f"Octal representation of {num} is: {octal_representation}")

# # Ques 18 (c) printing factorial of a number
# def factorial_num(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial_num(n-1)

# n = int(input("Enter a number: "))
# print(f"Factorial of {n} is {factorial_num(n)}")

# # Ques 18 (d) printing first n terms of fibonacci series
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         series = fibonacci(n - 1)
#         series.append(series[-1] + series[-2])
#         return series

# n = int(input("Enter the number of terms: "))
# print(f"First {n} terms of Fibonacci series: {fibonacci(n)}")

# # Ques 18 (e) calculate geometric sum upto n terms
# def geometric_sum(n):
#     if n == 0:
#         return 1  
#     return 1 / (2 ** n) + geometric_sum(n - 1)

# n = int(input("Enter the number of terms: "))
# print(f"Geometric sum up to {n} terms is: {geometric_sum(n):.5f}")

# # Ques 19 To add all the items of a numeric list
# nums = [1, 2, 3, 4, 5]
# sum = sum(nums)
# print(f"Sum of list: {sum}")

# # Ques 20 find smallest and largest element of numeric list
# nums = [10, 5, 20, 8, 25, 3]
# min = min(nums)
# max = max(nums)
# print(f"Smallest: {min}, Largest: {max}")

# # Ques 21 Remove duplicates from list
# nums = [1, 2, 3, 5, 4, 5, 1, 6, 5]
# set_list = list(set(nums))
# print(f"List without duplicates: {set_list}")

# # Ques 22 Create a list by concatinating a given list from 1 to n
# # sample list [p , q] n =5
# # output list [p1,q1,p2,q2,p3,q3,p4,q4,p5,q5]

# sample_list = ['p', 'q']
# n = 5
# result = [item + str(i) for i in range(1, n + 1) for item in sample_list]
# print(result)