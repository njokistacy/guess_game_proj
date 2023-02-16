#This program demonstrates a guessing game
#STEPS
#1.Import the random module
from random import randint
#2.get player's name
player=input("What is your name?")
print("Hello there " + player +"!")

#3.generate a random number
rand_number=randint(10,50)

#4.Using a while loop limit the number of tries
counter=0
while counter<5:
    player_no=eval(input("Enter a random number between 10 and 50:"))
    counter=counter+1
#5.using a while loop:check if user input is equal to generated number
    if player_no<rand_number:
        print("Your guess is too low "+ player)
    elif player_no>rand_number:
        print("Your guess is too high "+ player)
    elif player_no==rand_number:
        print("You win the game")
        break

print("GAME OVER!The correct number is",rand_number)
    




