#Ques-7 Write python script to find sum of first n natural numbers
n = int(input("Enter a number : "))
sum=0
for i in range(1, n+1):
    sum = sum + i
print("Sum is : ", sum)