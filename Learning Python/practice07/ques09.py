n=int(input("Enter the number of rows: "))
print("*"*n)
for i in range(n-2):
    print("*"*1, end="")
    for j in range(n-2):
        print(" ", end="")
    print("*")
print("*"*n)