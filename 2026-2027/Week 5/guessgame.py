import random
number= random.randint(1,100)
attempts = 0
while True:
    guess = int(input("Try to guess the number, idiot"))
    attempts +=1
    if guess< number:
        print("too low! you fool.")
    elif guess>number:
        print("too high! moron.")
    else:
        print("congrats! you are correct")
        print("amount of atempts:", attempts)