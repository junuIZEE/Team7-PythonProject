def getInt(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a number.")

def Bilal():
    x=getInt("Enter first number: ")
    y= getInt("Enter second number: ")
    Ans=0.0
    Operation=getInt("1.\tAdd\n2.\tSubtract\n3.\tMultiply\n4.\tDivide\n")

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

    print("Answer:",Ans)

def main():

    Bilal()

if __name__ == "__main__":
    main()







