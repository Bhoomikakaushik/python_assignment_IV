#Ques - 14 Write a python script to find whether a given number is armstrong number or not
n = int(input("Enter a number : "))
original_num = n
sum=0
digit = 0
while n > 0:
    digit = n % 10
    sum = sum + digit**3
    n = n // 10
if(original_num == sum):
    print(f"{original_num} is an armstrong number")
else:
    print(f"{original_num} is not an armstrong number")