import random
number_to_be_guessed = random.randint(1,9)
chances = 0
while chances<5 : 
    guess = int(input("Enter your guess"))
    #Compare the user guessed number with the computer number
    if guess == number_to_be_guessed:
        print("Congratulations! You win!")
        break
    elif guess < number_to_be_guessed:
        print("Guess is too low. Try a higher number than", guess)
    else :
        print("Guess was too high. Try a lower number than", guess)
    chances += 1
if not chances<5:
    print("You lost the game. The correct number was", number_to_be_guessed)