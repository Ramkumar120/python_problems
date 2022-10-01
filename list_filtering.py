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