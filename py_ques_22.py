# Ques 22 Create a list by concatinating a given list from 1 to n
# sample list [p , q] n =5
# output list [p1,q1,p2,q2,p3,q3,p4,q4,p5,q5]

sample_list = ['p', 'q']
n = 5
result = [item + str(i) for i in range(1, n + 1) for item in sample_list]
print(result)