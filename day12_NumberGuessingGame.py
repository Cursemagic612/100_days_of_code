import art
import random

end = False
lives = -1
difficulty = ""
guess_value = -1

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of the a number between 1 and 100.")

#Let user choose the difficulty and set the lives
while difficulty != "easy" or difficulty == "hard":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    lives = 10
else:
    lives = 5

#Random a number
rand_num = int(random.randint(1,100))

#Loop while it is not end yet
while end is False:
    #Check if lives is higher than 0
    if lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess_value = int(input("Make a guess: "))

        #compare numbers and provide feedback
        if guess_value == rand_num:
            print(f"You got it! The answer is {rand_num}.")
            end = True
        elif guess_value < rand_num:
            print(f"Too Low.\nGuess Again")
            lives -= 1
        elif guess_value > rand_num:
            print(f"Too High.\nGuess Again")
            lives -= 1
        else:
            print("Errors. Please fix it.")
    else:
        print(f"You've run out of guesses. The correct answer is: {rand_num}.\nGood luck next time.")
        end = True
