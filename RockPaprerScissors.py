import random
def rps():
        moves = ["rock","paper","scissors"]

        c_choice =random.choice(moves)

        playerchoice = input("choose a move (rock) (paper) (scissors): ").lower()

        if playerchoice in moves:
                print(f"computer move: {c_choice}")
        
                if playerchoice == "rock" and c_choice == "scissors":
                        print("you won")
                elif playerchoice == "scissors" and c_choice == "rock":
                        print("computer won")
                elif playerchoice == "paper" and c_choice == "scissors":
                        print("computer won")
                elif playerchoice == "scissors" and c_choice == "paper":
                        print("you won")
                elif playerchoice == "rock" and c_choice == "paper":
                        print("computer won")
                elif playerchoice == "paper" and c_choice == "rock":
                        print("you won")
                if  playerchoice == c_choice:
                        print("draw")

        else:
                rps()
while True:
        play = input("play a game y/n: ")
        if play == "y" :
                 rps()
        elif play == "n":
                break


        






