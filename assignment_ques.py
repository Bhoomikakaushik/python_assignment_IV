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

