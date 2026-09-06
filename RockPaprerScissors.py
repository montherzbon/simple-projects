import random
def rps():
        moves = ["rock","paper","scissors"]

        c_choice =random.choice(moves)

        playerchoice = input("choose a move (rock) (paper) (scissors): ")

        if playerchoice in moves:
                print(f"computer move: {c_choice}")
        
                if playerchoice == "rock" and c_choice == "scissors":
                        print("u won")
                elif playerchoice == "scissors" and c_choice == "rock":
                        print("computer won")
                elif playerchoice == "paper" and c_choice == "scissors":
                        print("computer won")
                elif playerchoice == "scissors" and c_choice == "paper":
                        print("u won")
                elif playerchoice == "rock" and c_choice == "paper":
                        print("computer won")
                elif playerchoice == "paper" and c_choice == "rock":
                        print("u won")
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


        






