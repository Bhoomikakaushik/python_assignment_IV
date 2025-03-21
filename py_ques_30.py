# Ques - 30 To check whether a list is sorted or not 
numbers = [ 1,3,6,8,4,5]

def is_sorted(numbers):
    result = numbers == sorted(numbers)
    return result

print( is_sorted(numbers))