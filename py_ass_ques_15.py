#Ques- 15 Write a python script to print all palindromes for a range 500-1000
for i in range(500,1000):
    i = str(i)
    reverse = i[::-1]
    if(reverse == i):
        print(i,end=" ")