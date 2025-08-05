import random
a=["rock","paper","scissors"]
x=random.choice(a)
b=input("choose rock or paper or scissors")
print("computers choice is",x)
if x=="rock" and b=="scissors":
        print("computer wins")
elif x=="paper" and b=="rock":
        print("computer wins")
elif x=="paper" and b=="paper":
        print("draw")
elif x=="paper" and b=="scissors":
        print("user wins")
elif x=="rock" and b=="rock":
        print("draw")
elif x=="rock" and b=="paper":
        print("user wins")
elif x=="scissors" and b=="paper":
            print("computer wins")
elif x=="scissors" and b=="scissors":
            print("draw")
elif x=="scissors" and b=="rock":
            print("user wins")
else :
            print("invalid")            
            

        

