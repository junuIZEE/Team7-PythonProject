from random import randint as rnd
def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")

def Jyotish():
    print("A random number from 1 to 50 has been chosen")
    print("You must try to guess it!\n")

    while True:
        # Secret number that the user must guess
        secret = rnd(1, 50)

        # Guesses made
        guesses = 0 
        
        while True:
            print("Enter a number between 1 and 50")
            guess = getInt("")
            guesses += 1

            if guess < secret:
                print("Too low")
            elif guess > secret:
                print("Too high")
            else:
                break

        print(f"\nCorrect! It took you {guesses} guesses")
        print("to reach the right number.")

        inp = input("\nPlay again? (y/n) ")
        if inp in ['n', 'N']:
            break


Jyotish()
