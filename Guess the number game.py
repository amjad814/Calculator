import random

print("Welcome To Guess The Number Game!")

secret_number = random.randint(1, 100)
# computer choose the random number
attempts = 0

while True:
    Guess = int(input("Enter your Guess: "))

    attempts +=1

    if Guess < secret_number:
        print("To low ! Try Again")

    elif Guess > secret_number:
        print("To high ! Try Again")
    else:
        print(f"congratulations! you guessed the number in {attempts} atempts")
        break
