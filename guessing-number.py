import random

n = random.randrange(1,100)

guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter nummber again: "))
        
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")            