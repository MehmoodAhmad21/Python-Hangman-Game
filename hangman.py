import random as r

class HangmanGame:
    def __init__(self, filename='hangman_words.txt'):
        self.word_list = self.read_file(filename)

    def read_file(self, filename):
        word_list = []
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().lower()
                word_list.append(word)
        return word_list

    def play_game(self):
        while True:
            random_word = r.choice(self.word_list)
            correct_guessed_letters = set()
            max_attempts = 10
            incorrect_guessed_letters = set()

            while True:
                display_word = ""
                for letter in random_word:
                    if letter in correct_guessed_letters:
                        display_word += letter
                    else:
                        display_word += "_"

                print(display_word)

                if set(display_word) == set(random_word):
                    print(f"Correct! The word is {random_word}")
                    break

                guess = input("Enter a letter: ").lower()

                if guess.isalpha() and len(guess) == 1:
                    if guess in correct_guessed_letters or guess in incorrect_guessed_letters:
                        print("You already guessed that letter. Try again.")
                    elif guess in random_word:
                        correct_guessed_letters.add(guess)
                    else:
                        max_attempts -= 1
                        incorrect_guessed_letters.add(guess)
                        print(f"Wrong! {guess} is not correct. Remaining attempts: {max_attempts}")

                    if max_attempts == 0:
                        print(f"You lose! The correct word was {random_word}")
                        break
                else:
                    print("Please enter a valid single letter.")

            if not self.play_again():
                break

    def play_again(self):
        while True:
            user = input("Would you like to play again? (Y/N) ").upper()
            valid_input = ["Y", "N"]

            if user not in valid_input:
                print("Invalid input, please enter again.\n")
            elif user == "Y":
                return True
            else:
                return False

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.play_game()
