'''
Question:
Find the number of times a sub string is repeated in a string 
eg:  hai   is repeated   3 times  in  hellohaihellohaiareyoutherehaihello
'''

def sub_string(string,substring):
    print(string.count(substring))
    
count=int(input())
for iteration in range(count):
    string,substring=input().upper().split()
    
    sub_string(string,substring)