list1=[]
for i in range(4):
    elem=int(input(f"Enter {i+1}st number "))
    list1.append(elem)
list1.sort(reverse=True)
print(list1[0])    