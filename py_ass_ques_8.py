#Ques-8 Write python script to find factorial of a given number
n = int(input("Enter a number : "))
fact=1
for i in range(1, n+1):
    fact = fact * i
print("Factorial is : ", fact)