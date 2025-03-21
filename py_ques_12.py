#Ques-12 Write a python script to print fibonacci series upto n terms
n = int(input("Enter a number : "))
count = 0 
a = 0 
b = 1
print(a , end=" ")
print(b , end=" ")
fib = 0
while( n-2 > count):
    fib = a + b
    print(fib , end=" ")
    a = b
    b = fib
    count = count + 1