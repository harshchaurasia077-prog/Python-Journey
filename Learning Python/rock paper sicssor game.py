import random
state=0
def gamewin(comp,you):
    if comp==you:
        state=2
    elif comp=="r":
        print("Computer choice is Rock")
        if you=="p":
            state=1
        elif you=="s":
            state=0
        else:
            state=2
    elif comp=="p":
        print("Computer choice is paper")
        if you=="r":
            state=0
        elif you=="s":
            state=1
        else:
            state=2
    elif comp=="s":
        print("Computer choice is sicssor")
        if you=="p":
            state=0
        elif you=="r":
            state=1
        else:
            state=2
    return state
you=input("Enter your choice, rock(r), paper(p),sisscor(s):")
comp=random.randint(1,3)
if comp==1:
    comp="r"
elif comp==2:
    comp="p"
else:
    comp="s"
state=gamewin(comp,you)
if state==1:
    print("You Won")
elif state==2:
    print("Match draw")
else:
    print("You lose")
