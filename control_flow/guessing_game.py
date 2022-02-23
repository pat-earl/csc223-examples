import random
winning_guess = random.randint(0, 100)
print(winning_guess)
num_of_guesses = 0
won = False

# while won == False
while not won:
    try:
        guess = int(input("Please enter a guess between 0 & 100: "))
        num_of_guesses += 1
    except ValueError:
        print("Please enter digits!")
        continue
    

    if guess == winning_guess:
        won = True
    elif guess > winning_guess:
        print("Guess is too high! Try again...")
    else:
        print("Guess is too low! Try again...")

print("Congrats! You won")
print("It took you", num_of_guesses, "tries!")