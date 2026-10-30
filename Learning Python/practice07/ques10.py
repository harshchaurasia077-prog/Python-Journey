n=int(input("Enter the number: "))
mul=[]
for i in range(1,11):
    mul.append(n*i)
mul.reverse()
for j in mul:
    print(f"{n}*{10-mul.index(j)}={j}")