#Ques-6 Write a python script to find given number is prime or composite
n = int(input("Enter a number : "))
for i in range(2,n):
    if(n%i == 0):
        print(f"{n} is a composite number")
        break
else:
    print(f"{n} is prime number")