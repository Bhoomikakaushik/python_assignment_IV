# Ques - 27 to find all the numbers of a list that are divisible by a particular element

numbers = [2,4,3,6,8,5]
element = int(input("Write a number through which you want to divde the list numbers : "))
answer = list(filter(lambda x:x % element == 0, numbers))

print(answer)