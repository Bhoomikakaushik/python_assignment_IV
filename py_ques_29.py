# Ques - 29 to print table of 10 upto users choice using lambda list comprehension

n = int(input("Enter the number upto which you want to print the table : "))
# answer = list(lambda x : x * 10 )(x) for x in range(n + 1)
answer = [(lambda x: 10 * x)(x) for x in range(1, n + 1)]

print(answer)