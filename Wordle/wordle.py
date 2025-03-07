import random
word_list = [
    "apple", "brave", "candy", "delta", "eagle", "flame", "grape", "happy", "jolly", "kites",
    "lemon", "mango", "novel", "ocean", "piano", "queen", "raven", "smile", "tiger", "uncle",
    "vivid", "whale", "xenon", "youth", "zebra", "frost", "cloud", "glove", "spoon", "light",
    "track", "charm", "grasp", "bloom", "daisy", "brisk", "flock", "swoop", "fable", "quilt",
    "shine", "grove", "spike", "flair", "vapor", "quirk", "witty", "crisp", "lunar", "blink"
]

word = random.choice(word_list)
guessed = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print("\nCurrent word: " + ' '.join(guessed))
    guess = input("Guess a letter: ").lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!\nYou have " + str(attempts) + " attempts left.")
    
    if '_' not in guessed:
        print("\nCongratulations! You have guessed the word: " + word + "\n")
        break
else:
    print("\nYou've run out of attempts! The word was: " + word)