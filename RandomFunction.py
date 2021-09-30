#functions 
import random

#WE ARE GOING TO CREATE A GUESSING GAME

number = random.randint(1,10)

IsGuessRight = False

while IsGuessRight !=True :
    guess = input("please guess any number between 1 to 10 : ")
    if str(guess) == "hello" :
        print(" you have guessed the right number ")
        IsGuessRight = True
        continue
    elif str(guess) == "quit":
        break
    else:
        print("please try again ")

