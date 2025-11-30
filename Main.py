from random import randint as rnd

def get_num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a number.")

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
            guess = get_num("")
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

def Bilal():
    x=get_num("Enter first number: ")
    y= get_num("Enter second number: ")
    Ans=0.0
    Operation=get_num("1.\tAdd\n2.\tSubtract\n3.\tMultiply\n4.\tDivide\n")

    if Operation==1:
        Ans=x+y
    elif Operation==2:
        Ans=x-y
    elif Operation==3:
        Ans=x*y
    elif Operation==4:
        if y!=0: Ans=x/y
        else:print("Invalid input\n")
    else:
        print("Invalid input\n")

    print("Answer:", Ans)

def main():
    Jyotish()
    Bilal()

if __name__ == "__main__":
    main()
