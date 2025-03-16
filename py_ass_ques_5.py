#Ques-5 Write python script to find given number is leap year or not
n = int(input("Enter a number to find given number is leap year or not : "))
if((n%4==0 and n%100 != 0) or (n%400 == 0)):
    print(f"{n} is leap year")
else:
    print(f"{n} is not a leap year")