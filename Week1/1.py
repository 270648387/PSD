import random

def word_guessing():
    word_list = ['python', 'software', 'engineering', 'professional']

    while True:  # Outer loop to allow replay
        word = random.choice(word_list)
        blanks = ['_'] * len(word)
        lives = 10

        print("\nWord Guessing")
        print("You have", lives, "lives")
        print("The word has", len(word), "letters")

        while True:  # Inner loop for one game
            print("\nWord:", ' '.join(blanks))
            guess = input("\nGuess a letter: ").lower()

            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        blanks[i] = guess
            else:
                lives -= 1
                print("Wrong guess! Lives left:", lives)

            if '_' not in blanks:
                print("\nCongrats! You guessed the word:", word)
                print("GAME OVER")
                break

            if lives == 0:
                print("\nGAME OVER. The word was:", word)
                break

        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Run the game
word_guessing()
