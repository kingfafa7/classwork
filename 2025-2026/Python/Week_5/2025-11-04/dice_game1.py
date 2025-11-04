import random
from itertools import repeat


def main():
    print()
    #Mustafa Hasan ALi
    #11/04/2025
    answer =input("How many times would you like to roll a single sided die?")
    for i in range(0,int(answer)):
        number = random.randint(1, 6)
        print("You rolled a " + str(number))

if __name__ == '__main__':
    main()
