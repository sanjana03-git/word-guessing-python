import random

word_bank = ["python", "java", "javascript", "ruby", "swift",]

word = random.choice(word_bank)

guessedWord = ["_"] * len(word) #placeholders for letters

attempts = 6  # Set the number of allowed attempts

while attempts > 0:
    print("Current word: " + " ".join(guessedWord))

    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: " + str(attempts))

    if "_" not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break

    if attempts == 0 and "_" in guessedWord:
        print("\nYou have run out of attempts! The word was: " + word)
