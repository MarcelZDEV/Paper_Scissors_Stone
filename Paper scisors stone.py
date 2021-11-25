import random
import sys

options_list = ("paper", "stone", "scissors")

win = 10
lose = -5
points = 0

while True:
    random_option = random.choice(options_list)

    user_input = input("chose option: ")

    if user_input == "scissors" and random_option == "paper":
        points = points + win
        print("Your score is: " + str(points))
    elif user_input == "stone" and random_option == "scissors":
        points = points + win
        print("Your score is: " + str(points))
    elif user_input == "paper" and random_option == "stone":
        points = points + win
        print("Your score is: " + str(points))

    # user lose
    elif user_input == "paper" and random_option == "scissors":
        points = points + lose
        print("Your score is: " + str(points))
    elif user_input == "stone" and random_option == "paper":
        points = points + lose
        print("Your score is: " + str(points))
    elif user_input == "scissors" and random_option == "stone":
        points = points + lose
        print("Your score is: " + str(points))

    #Same
    elif user_input == "paper" and random_option == "paper":
        print("Your score is: " + str(points))
    elif user_input == "stone" and random_option == "stone":
        print("Your score is: " + str(points))
    elif user_input == "scissors" and random_option == "scissors":
        print("Your score is: " + str(points))
    #end
    elif user_input == "99":
        sys.exit()
    else:
        print("404 :)")
