import random

class WordGuessingGame:
    def __init__(self):
        self.word_list = ['python', 'software', 'engineering', 'professional']
        self.lives = 10
        self.word = ''
        self.blanks = []

    def choose_word(self):
        self.word = random.choice(self.word_list)
        self.blanks = ['_'] * len(self.word)
        self.lives = 10

    def display_status(self):
        print("\nWord:", ' '.join(self.blanks))
        print("Lives left:", self.lives)

    def get_guess(self):
        return input("\nGuess a letter: ").lower()

    def update_blanks(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.blanks[i] = guess

    def play_round(self):
        self.choose_word()
        print("\nWord Guessing Game ")
        print("The word has", len(self.word), "letters")

        while True:
            self.display_status()
            guess = self.get_guess()

            if guess in self.word:
                self.update_blanks(guess)
            else:
                self.lives -= 1
                print("Wrong guess!")

            if '_' not in self.blanks:
                print("\nCongrats! You guessed the word:", self.word)
                print("GAME OVER")
                break

            if self.lives == 0:
                print("\nGAME OVER. The word was:", self.word)
                break

    def play(self):
        while True:
            self.play_round()
            again = input("\nDo you want to play again? (y/n): ").lower()
            if again != 'y':
                print("Thanks for playing!")
                break

# Run the game
if __name__ == "__main__":
    game = WordGuessingGame()
    game.play()
