import random
import time

def start_game():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You are standing in front of a dark cave.")
    time.sleep(1)
    choice = input("Do you want to enter the cave? (yes/no) ")
    
    if choice.lower() == "yes":
        enter_cave()
    else:
        print("You walk away from the cave. The adventure ends.")
    
def enter_cave():
    print("You enter the cave and hear growling sounds.")
    time.sleep(1)
    choice = input("Do you want to fight or run? (fight/run) ")
    
    if choice.lower() == "fight":
        fight()
    elif choice.lower() == "run":
        run_away()
    else:
        print("Invalid choice. You stand still, and the monster attacks you.")
    
def fight():
    print("You fight the monster bravely...")
    time.sleep(1)
    if random.random() > 0.5:
        print("You win the fight and find treasure!")
    else:
        print("You lose the fight. Better luck next time.")

def run_away():
    print("You run away safely, but you miss the treasure.")
    print("The adventure ends.")

start_game()
