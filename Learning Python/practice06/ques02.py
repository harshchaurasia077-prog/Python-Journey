totalmarks=int(input("enter the total marks of the each subjects"))
a=int(input("Enter first subject number:"))
apercent=(a/totalmarks)*100
b=int(input("Enter second subject number:"))
bpercent=(b/totalmarks)*100
c=int(input("enter third subject number:"))
cpercent=(c/totalmarks)*100
if(apercent<33 or bpercent<33 or cpercent<33):
    print("You are fail ")
elif((a+b+c)*100/3>=40):
    print("You are passed")
else:
    print("You are failed")
   