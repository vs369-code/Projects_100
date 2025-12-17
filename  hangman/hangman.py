import random
from hangman_word import word_list 
from hangman_art import stages,logo 



lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    print(f"***********************{lives}<???>/6 LIVES LEFT*************************")
    guess = input("Guess a letter:").lower()

    if guess in correct_letter:
        print(f"you've already guessed {guess}")
 

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"  

    print("Word to guess:" + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. you lose a life.")
        if lives == 0:
            game_over = True
            print(F"**********************IT WAS {chosen_word}! YOU LOSE*******************")


    if "_" not in  display:
        game_over = True
        print("You win.")

    print(stages[lives])