"""Print m numbers n times"""
print ("Input number of integers to be printed")
m=int(input())
print ("Input Number of times, these numbers to be printed")
n=int(input())
for i in range(n):
    for j in range(m):
        print(j, end=" ")
    print(" ")
