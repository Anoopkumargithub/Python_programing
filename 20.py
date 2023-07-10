print("Guess The Number")
print("Welcome To Our Game")
print("Warning\nYou have only 5 chance to win this game")
print("Now\nWe Start The Game")
print("Guess the number which is greater than 5 and lesser than 100 \nthis number is can divided by all even number and it can divided by 5 also ")
n = 30
i = 0
while(i<5):
    a = int(input(f"Enter Your Number, Chance No. - {i+1}\n"  ))
    if a<30:
        print("Try Again" )
    elif a>30:
        print("Try Again" )
    else :
        print("Congrugulation\nYou Win This Game")
        break
    i = i+1
