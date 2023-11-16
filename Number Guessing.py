#   import essential modules
import random
import math

#   define variables
Count = 0

#   get range of numbers from user
Lower = int(input("Please Enter The Lower Band Number : "))
Upper = int(input("Please Enter The Upper Band Number : "))
print("Your Start band is {} and your end is {}".format(Lower, Upper))

#   generate random number from range of numbers which is between Lower and Upper
RandomNumber = random.randrange(Lower, Upper)
print(RandomNumber)

#   calculate the chance of guessing
Chance = round(math.log(Upper - Lower + 1, 2))
print("you have {} CHANCES to guess !!!!!! ".format(Chance))

#   main loop to check the answer from the user
while Count < math.log(Upper - Lower + 1, 2):
    Count = Count + 1
    Num = Chance - Count
    Guess = int(input("Please Enter The Guess Number : "))
    if RandomNumber == Guess:
        print("You Won , congratulations! You find the number in {} guess".format(Count))
        break
    elif Guess < RandomNumber:
        print("You Lost , Try Higher Number")
    elif Guess > RandomNumber:
        print("You Lost , Try Lower Number")
    if Num == 0:
        print("This is your final guess!!!!!! ")
    else:
        print("You have {} CHANCES to guess!!!!!! ".format(Num))

    if Count > math.log(Upper - Lower + 1, 2):
        print("Lost , The correct number is : {} , Maybe more lucky tomorrow".format(RandomNumber))
