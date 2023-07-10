import random
print("Number of rounds you want to play :")
rounds = int(input())
draw_rounds = 0
p_point = 0
c_point = 0

while (rounds>0):

     cpu_moves = ["Snake", "Water" , "Gun"]
     cpu_choice = random.choice(cpu_moves)

     print("\nEnter player choice : ")
     player_choice = input()

     print("cpu choice :", cpu_choice)
     if player_choice == "Snake":
         if cpu_choice == "Snake":
            print("Draw")
            draw_rounds += 1

         elif cpu_choice == "Water":
            print("Win")
            p_point +=1
         else :
            print("Lose")
            c_point += 1

     elif player_choice == "Water":
        if cpu_choice == "Snake":
           print("Lose")
           c_point += 1
        elif cpu_choice == "Water":
           print("Draw")
           draw_rounds += 1
        else :
           print("Win")
           p_point += 1

     else:
        if cpu_choice == "Gun":
           print("Draw")
           draw_rounds += 1
        elif cpu_choice == "Water":
           print("Lose")
           c_point += 1
        else:
           print("Win")
           p_point += 1
     rounds -= 1

print("\nTotal Score at the end of  rounds")

print("\nNo. of rounds draw between cpu and player :")
print(f"{draw_rounds} rounds")
print("\nNo. of rounds player won:")
print(f"{p_point} rounds")
print("\nNo. of rounds cpu won :")
print(f"{c_point} rounds")