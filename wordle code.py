import random

#selecting a word
def select_word(wordle_words):
    with open(wordle_words, 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()

#cheaking the guess
def check_guess(secret_word, guess):
    result = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            result += guess[i].upper() + ' '
            # Correct letter in the right place
        elif guess[i] in secret_word:
            result += guess[i].lower() + ' '
            # Correct letter in the wrong place
        else:
            result += '-' + guess[i] + '-' + ' '
            # Incorrect letter
    return result

#the game
def play_wordle(wordle_words,level):
    secret_word = select_word(wordle_words)

    #3-letter
    if level==3:
        attempts = 10
        guessed = False
        print("Welcome to Wordle! Guess the 3-letter word.")
        print("__________")
        #Rules
        print("Instructions:")
        print("- Guess a 3-letter word.")
        print("- The word may contain lowercase letters, uppercase letters, or a combination of both.")
        print("- If a letter is in the word and used at the right place, it will be printed in uppercase.")
        print("- If a letter is in the word but not at the correct place, it will be printed in lowercase.")
        print("- If a letter is not in the word, it will be displayed with a cut (-) on both sides.")
        print("- You have 10 attempts to guess the word.")
        print("_______________")

        #guessing
        while attempts > 0 and guessed == False: 
            guess = input("Enter your guess: ").strip().lower()
            #invalid word input
            if len(guess) != 3: 
                print("Invalid guess. Please enter a 3-letter word.")
                continue
            attempts -= 1
            result = check_guess(secret_word, guess)
            #correct
            if secret_word.upper() == guess.upper(): 
                guessed = True
            else:
               print("Attempt remaining:", attempts)
               print("Result:", result)
        #won
        if guessed: 
            print("Congratulations! You guessed the word correctly:", secret_word)
        #lost
        else:
            print("Sorry, you ran out of attempts. The word was:", secret_word)

    #4-letter
    if level==4:
        attempts = 6
        guessed = False
        print("Welcome to Wordle! Guess the 4-letter word.")
        print("__________")
        #Rules
        print("Instructions:")
        print("- Guess a 4-letter word.")
        print("- The word may contain lowercase letters, uppercase letters, or a combination of both.")
        print("- If a letter is in the word and used at the right place, it will be printed in uppercase.")
        print("- If a letter is in the word but not at the correct place, it will be printed in lowercase.")
        print("- If a letter is not in the word, it will be displayed with a cut (-) on both sides.")
        print("- You have 6 attempts to guess the word.")
        print("_______________")

        #guessing
        while attempts > 0 and guessed == False: 
            guess = input("Enter your guess: ").strip().lower()
            #invalid word input
            if len(guess) != 4: 
                print("Invalid guess. Please enter a 4-letter word.")
                continue
            attempts -= 1
            result = check_guess(secret_word, guess)
            #correct
            if secret_word.upper() == guess.upper(): 
                guessed = True
            else:
               print("Attempt remaining:", attempts)
               print("Result:", result)
        #won
        if guessed: 
            print("Congratulations! You guessed the word correctly:", secret_word)
        #lost
        else:
            print("Sorry, you ran out of attempts. The word was:", secret_word)

    #5-letter
    if level==5:
        attempts = 6
        guessed = False
        print("Welcome to Wordle! Guess the 5-letter word.")
        print("__________")
        #Rules
        print("Instructions:")
        print("- Guess a 5-letter word.")
        print("- The word may contain lowercase letters, uppercase letters, or a combination of both.")
        print("- If a letter is in the word and used at the right place, it will be printed in uppercase.")
        print("- If a letter is in the word but not at the correct place, it will be printed in lowercase.")
        print("- If a letter is not in the word, it will be displayed with a cut (-) on both sides.")
        print("- You have 6 attempts to guess the word.")
        print("_______________")

        #guessing
        while attempts > 0 and guessed == False: 
            guess = input("Enter your guess: ").strip().lower()
            #invalid word input
            if len(guess) != 5: 
                print("Invalid guess. Please enter a 5-letter word.")
                continue
            attempts -= 1
            result = check_guess(secret_word, guess)
            #correct
            if secret_word.upper() == guess.upper(): 
                guessed = True
            else:
               print("Attempt remaining:", attempts)
               print("Result:", result)
        #won
        if guessed: 
            print("Congratulations! You guessed the word correctly:", secret_word)
        #lost
        else:
            print("Sorry, you ran out of attempts. The word was:", secret_word)

    #6-letter
    if level==6:
        attempts = 10
        guessed = False
        print("Welcome to Wordle! Guess the 6-letter word.")
        print("__________")
        #Rules
        print("Instructions:")
        print("- Guess a 6-letter word.")
        print("- The word may contain lowercase letters, uppercase letters, or a combination of both.")
        print("- If a letter is in the word and used at the right place, it will be printed in uppercase.")
        print("- If a letter is in the word but not at the correct place, it will be printed in lowercase.")
        print("- If a letter is not in the word, it will be displayed with a cut (-) on both sides.")
        print("- You have 10 attempts to guess the word.")
        print("_______________")

        #guessing
        while attempts > 0 and guessed == False: 
            guess = input("Enter your guess: ").strip().lower()
            #invalid word input
            if len(guess) != 6: 
                print("Invalid guess. Please enter a 6-letter word.")
                continue
            attempts -= 1
            result = check_guess(secret_word, guess)
            #correct
            if secret_word.upper() == guess.upper(): 
                guessed = True
            else:
               print("Attempt remaining:", attempts)
               print("Result:", result)
        #won
        if guessed: 
            print("Congratulations! You guessed the word correctly:", secret_word)
        #lost
        else:
            print("Sorry, you ran out of attempts. The word was:", secret_word)

#running the game
print("Welcome to WORDLE: THE WORD GAME")
print('')
print("We have different levels you can play from:")
print("Easy mode (3-letter word)")
print("Normal mode (4-letter word)")
print("Hard mode (5-letter word)")
print("God mode (6-letter word)")


#selecting level
level=int(input("Enter the number of letter corresponding to the difficulty you want to play on:"))
if level==3:
    word_file = "wordle_words(3).txt" 
    play_wordle(word_file,level)
elif level==4:
    word_file = "F:\School project\wordle_words(4).txt" 
    play_wordle(word_file,level)
elif level==5:
    word_file = "" 
    play_wordle(word_file,level)
elif level==6:
    print("damn, good luck!")
    word_file = "wordle_words(6).txt" 
    play_wordle(word_file,level)
else:
    print("We Don't Do That Here -late Chadwick Boseman")

#end


