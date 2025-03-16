#Ques- 11 Write a python script to find whether given number is palindrome or not
n = input("Enter a number : ")
reverse = n[: : -1]
if(n==reverse):
    print(f"{n} is palindrome")
else:
    print(f"{n} is not a palindrome")