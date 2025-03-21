# Ques- 16-(a) Print following patterns
# *
# **
# ***
# ****
n = int(input("Enter a number upto which row you want to print the pattern a : "))
i = 0
while (i < n):
    j = 0
    while ( j <= i):
        print("*", end=" ")
        j = j + 1
    print("\n")    
    i=i+1


# Ques 16(b)
# ****
# ***
# **
# *
n = int(input("Enter a number upto which row you want to print the pattern b : "))
i = 1
while (i <= n):
    j = n
    while ( j >= i):
        print("*", end=" ")
        j = j - 1
    print("\n")    
    i=i+1


# Ques 16 (c)
#     *
#   * * *
#  * * * * *
n =  int(input("Enter a number upto which row you want to print the pattern c : "))
i = 0
while( i < n):
    j = n - i
    while( j > 0 ):
        print( " " , end = " ")
        j = j - 1
    # print("\n")
    
    j = 0
    while( j <= i):
        print("*" , end = " ")
        j = j + 1

    j = 1
    while(j <= i):
        print("*" , end = " ")
        j = j + 1
    print("\n")
    i = i + 1


# Ques 16 (d)
# 1
# 22
# 333
# 4444
n =  int(input("Enter a number upto which row you want to print the pattern d : "))
i = 1
while(i <= n):
    j = 1
    while( j <= i):
        print(i , end=" ")
        j = j + 1
    print("\n")
    i = i + 1


# Ques 16 (f)
# 1
# 2 3
# 4 5 6
# 7 8 9 10
n = int(input("Enter a number upto that row you want to print floyds triangle : "))
i = 0
count = 1
while( i < n):
    j = 0
    while( j <= i):
        print(count , end=" ")
        count = count + 1
        j = j + 1
    print("\n")
    i = i + 1