from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
def randomNumber():
    randomBound = input("Enter the bounds of the random number:\n")
    x = randomBound.split(",")
    print(randint(int(x[0]), int(x[1])))




