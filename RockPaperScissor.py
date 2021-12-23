import random
import os

End_input = "N"

while (End_input == "N" or End_input == "n") :
    result = os.system('clear')
    computer_choice = random.choice(['scissors', 'rock', 'paper'])
        # print("Computer choice is", computer_choice)
    user_choice = input ('Do you want - rock, paper or scissors \n')
        #print ("Guests Choice is ", user_choice)
    if user_choice == computer_choice:
        print ("TIE")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print ("You Win, Computer had", computer_choice)
    elif user_choice == 'paper' and computer_choice == 'rock':
        print ("You Win, Computer had", computer_choice)
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print ("You Win, Computer had", computer_choice)
    else :
        print ("Computer Wins !! Computer had", computer_choice)
    
    End_input = input ("Do you want to end the game? Enter (Y or N) \n : ")
    result = os.system('clear')