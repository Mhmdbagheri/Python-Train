import random
from collections import Counter


someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords)
print(word)

chance = len(word) + 2
print(chance)
letterguessed = ''
correct = 0
flag = 0

try:
    while(chance != 0) and flag == 0:
        chance -= 1

        try:
            guess = str(input("\nplease guess a letter : "))
            print('this is your {} chance Go on :'.format(chance))
        except:
            print("JUST A LETTER !!!!!!")
            continue

        if not guess.isalpha():
            print("JUST A LETTER !!!!!!")
            continue
        elif guess in letterguessed:
            print("you have already guessed a letter")
            continue

        if guess in word :
            k = word.count(guess)
            for _ in range(k):
                letterguessed += guess

        for char in word:
            if char in letterguessed and (Counter(letterguessed) != Counter(word)):
                print(char, end=' ')
                correct += 1

            elif (Counter(letterguessed) == Counter(word)):

                print(word)
                flag = 1
                print('Congratulations, You won!')
                break
                break
            else:
                print('_', end=' ')

        if chance == 0:
            print()
            print("You lost !")
            print('The word was {}'.format(word))

except keyboardInterrupt:
    print()
    print("Bye")
    exit()



