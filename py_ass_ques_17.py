# Ques 17 Using functions write python script for
# (a) finding whether a given number is palindrome or not

def is_palindrome( n ):
    original_n = n
    reverse = n[ : : -1]
    if(reverse == original_n):
        print(f"{original_n} is Palindrome number")
    else:
        print(f"{original_n} is not a palindrome number")

n = input("Enter a number : ")
is_palindrome(n)


# Ques 17 (b) finding sum of first n natural numbers
def sum_natural_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

n = int(input("Enter a number : "))
print(f"Sum of first {n} natural numbers is {sum_natural_numbers(n)}")