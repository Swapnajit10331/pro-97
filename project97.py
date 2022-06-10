mygame="Number guessing game"
print(mygame)
chances=0
while chances < 5:
    number = input("Guess a number")
    if number >= 0 and number <=9:
        print("You won")
        break
    elif number>9:
        print("guess less")
    elif number<0:
        print("guess more")
    else:
        print('You lost')
