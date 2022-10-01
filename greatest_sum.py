'''
Question:

Find the greates sum of consicutive intigers in a list 
eg: sum of consicutive intigers in this list 2, 7, 10, 5, 6, 4  is  2+7=9, 7+10=17, 
10+5=15, 5+6=11, 6+4=10. of this 17 is the highest sum.
'''

def find_greatest_sum(b):
    newlist=[]
    for i in range (len(b)-1):
        add= b[i]+b[i+1]
        newlist.append(add)
    print(max(newlist))

test_cases = int(input())

for iteration in range(test_cases):
    s = input()
    a = s.split()
    b = [int(i) for i in a]

    find_greatest_sum(b)