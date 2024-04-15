import random
userPoints=0
computerPoints=0
def play(userChoice,computerChoice):
    global userPoints,computerPoints
    if (userChoice==3 and computerChoice==1 )or (userChoice==2 and computerChoice==3)or( userChoice==1 and computerChoice==2):
        print("************COMPUTER WINS************")
        computerPoints+=1
    if (userChoice==1 and computerChoice==3)or(userChoice==2 and computerChoice==1)or(userChoice==3 and computerChoice==2):
         print("************USER WINS************")
         userPoints+=1
    if userChoice== computerChoice:
         print("************GAME IN TIE************")
    if userChoice==4:
        print("************EVALUATING RESULT************")
        print("COMPUTER SCORE:",computerPoints)
        print("YOUR SCORE:",userPoints)
        if computerPoints>userPoints:
            print("************COMPUTER WIN THE GAME************")
            print("************WELL PLAYED************")
        if computerPoints<userPoints:
            print("CONGRATS, YOU WIN THE GAME")
    
print("ROCK PAPER SCISSOR")
print("1 FOR ROCK")
print("2 FOR PAPER")
print("3 FOR SCISSOR")
print("4 FOR RESULT")
print("5 FOR EXIT")
while True:
    userChoice=int(input("ENTER YOUR CHOICE:"))
    auto=[1,2,3]
    computerChoice=random.choice(auto)
    if userChoice in (1,2,3,4):
        play(userChoice,computerChoice)
    if userChoice==5:
        print("************GAME END************")
        break
else:
    print("************ENTER VALID CHOICE************")
