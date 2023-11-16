import random

choiceList = 'Rock,Scissors,Paper'
choiceList = choiceList.split(',')
CPUchoice = random.choice(choiceList)
CPUchoice = CPUchoice.lower()
print(CPUchoice)

playerchoice = ''

while not playerchoice.isalpha():
        playerchoice = str(input("Choose a random choice : "))
        if not playerchoice.isalpha():
            print('you must enter a valid choice!')
else:
        playerchoice = playerchoice.lower()

        if CPUchoice == playerchoice:
            print('PC choose : {} & you choose : {}'.format(CPUchoice,playerchoice))
            print('Draw')
        elif CPUchoice == 'paper' and playerchoice == 'scissors' or CPUchoice == 'scissors' and playerchoice == 'rock':
            print('PC choose : {} & you choose : {}'.format(CPUchoice,playerchoice))
            print("Player Won!")
        else:
            print('PC choose : {} & you choose : {}'.format(CPUchoice,playerchoice))
            print('PC Won!')

