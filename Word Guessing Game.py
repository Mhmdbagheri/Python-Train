import random

turns = 12
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
print(word)
guess = input(str("Guess a Word :"))
while turns > 0:
    failed = 0
    for char in word:
        if char in guess:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1
    if failed == 0:
        print("you won !")
        print("The word is : ", word)
        break

    guesses = input(str("\nGuess a Word :"))
    guess += guesses
    if guesses not in word:
        turns -= 1
        print("wrong")
        print("you have {} to guess".format(turns))