import random

print("Random Number Generator\n")

countNum = 1

while countNum <= 6: 
    print("Enter number input between 1-100: \n")
    x = input()
    print("You enter ", x)
    print("Let's see!!\n")

    num = random.randint(0, 100)

    print('You generate ' + (str(countNum)) + ' number')

    if x == num:
        print(num , " is your number")
        break
    if x != num:
        print("You have to enter the number again")
        print("Go back to enter number input")
        countNum += 1
        if countNum == 6:
            print("GAME OVER!")
            print("The number is ", num)
            break
