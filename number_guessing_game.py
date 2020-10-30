#Number guessing game
from random import randint
n=randint(1,500)
i=1
guess=int(input("enter a number between 1 to 500\t:-"))
while n!=guess:
    if guess<=0:print("Lost. Number was:-",n);break
    elif guess>n:print("Number Too Large.Try Again")
    else:print("Number Too Small.Try Again")
    guess=int(input("enter a number between 1 to 500\t:-"))
    i=i+1
else:print("Congratulations, You guessed is Right! after %d times"%i)
