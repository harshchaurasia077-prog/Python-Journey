n=int(input("Enter the number of fruits in the list"))
list1=[]
for i in range(n):
    fruitname=input(f"Enter the {i+1} Fruit name")
    list1.append(fruitname)
print(list1)    