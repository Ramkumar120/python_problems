'''
Question:
Find the greatest number in the list
eg: 10 is greatest in 2, 7, 10, 5, 6, 4
'''
#code:

def greatest_number(numbers):
    print(max(numbers))
    
count=int(input())
for iteration in range(count):
    a=input().split()
    numbers=[int(i) for i in a]
    
    greatest_number(numbers)

