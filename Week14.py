# Week 14 Homework
# Problem 1

def readposint():
    try:
        posint = int(input("Please enter your integer: "))
        if posint <=0:
            print("You did not enter a positive integer".format(posint))
        else: 
            print("You entered a positive integer".format(posint))
    except ValueError:
        print("That is not a positive integer. Please enter a positive integer.")
        return posint
readposint()

        
    
