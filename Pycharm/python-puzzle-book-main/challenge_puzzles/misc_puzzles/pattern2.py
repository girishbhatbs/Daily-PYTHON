print("Input number for which a 1-n matrix is created")
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print(" ")