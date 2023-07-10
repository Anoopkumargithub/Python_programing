#  Snake Water Gun
import random
from secrets import choice

print("Welcome To The Game")
print("The game of the Sanke, Water, & Gun")
# print("You have only 10 choice")
print("No. of rounds you want to play")
rounds = int(input())
draw_rounds = 0
p_rounds = 0
c_rounds = 0
i = 0
for i in range(1, rounds+1):
    print("Round no.", i)
    print("Press s for snake, Press w for water, press g for gun")
    a = input()
    if a == "s":
        pass
    elif a == "w":
        pass
    elif a == "g":
        pass
    else:
        print("Invalid\nRestart The Game")
        break
    list = ("snake", "water", 'gun')
    choice = random.choice(list)
    print(choice)
    if a == "s":
        if choice == "snake":
            print("Draw")
            draw_rounds += 1
        elif choice == "water":
            print("You Win")
            p_rounds += 1
        elif choice == "gun":
            print("Computer Win")
            c_rounds += 1
        else:
            pass
    elif a == "w":
        if choice == "snake":
            print("Computer Win")
            c_rounds += 1
        elif choice == "water":
            print("Draw")
            draw_rounds += 1
        elif choice == "gun":
            print("You Win")
            p_rounds += 1
        else:
            pass
    elif a == "g":
        if choice == "snake":
            print("You Win")
            p_rounds += 1
        elif choice == "water":
            print("Computer Win")
            c_rounds += 1
        elif choice == "gun":
            print("Draw")
            draw_rounds += 1
        else:
            pass
            break
    else:
        pass
        continue
    print("No. of turn's left",rounds-i)

print(f"Number of Turns You Win + {p_rounds}")
print(f"Number of Turns Computer Win + {c_rounds}")
print(f"Number of Turns Draw + {draw_rounds}")

if p_rounds>c_rounds:
    f1 = p_rounds
else:
    f1 = c_rounds

if c_rounds>draw_rounds:
    f2 = c_rounds
else:
    f2 = draw_rounds

if f1 == f2:
    print("Computer Win The Game")
elif f1 > f2 :
    print("You Win The Game")
elif f2 > f2 :
    print("Draw")

print("Thank You For Playing Game")


