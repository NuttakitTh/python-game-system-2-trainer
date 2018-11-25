import random

def genDigit():
    digit = ''
    while len(digit) != 4:
        if len(digit) == 0:
            num = random.randint(1,9)
            num = str(num)
            digit += num
        else:
            num = random.randint(0,9)
            num = str(num)
            digit += num
    return digit

def strToInt(x):
    x = int(x)
    return x
def intToStr(x):
    x = str(x)
    return x

def plus1(digit):
    newDigit = ''
    for l in digit:
        l = strToInt(l)
        l += 1
        if l == 10:
            l = 0
        l = intToStr(l)
        newDigit += l
    return newDigit
    
def plus3(digit):
    newDigit = ''
    for l in digit:
        l = strToInt(l)
        l += 3
        if l >= 10:
            l %= 10
        l = intToStr(l)
        newDigit += l
    return newDigit
    


def gameOver():
    print("Game over!!")
    print("Your longest streak is " + str(streak) + '.')
    flag = False
    
def add1():
    flag = True
    streak = 0 
    while flag:
        digit = genDigit() 
        print(digit)
        digit = plus1(digit)
        ans = input()
        if ans == digit:
            print("Correct!!")
            streak += 1
        else:
            print("Game over!!")
            print("Your longest streak is " + str(streak) + '.')
            flag = False
        
def add3():
    flag = True
    streak = 0 
    while flag:
        digit = genDigit() 
        print(digit)
        digit = plus3(digit)
        ans = input()
        if ans == digit:
            print("Correct!!")
            streak += 1
        else:
            print("Game over!!")
            print("Your longest streak is " + str(streak) + '.')
            flag = False
        
def sys2Game():
    while True:
        print("Welcome!!")
        print("Choose Your challenge.")
        print("Press 1 to choose Add1")
        print("Press 3 to choose Add3")
        print("Your choice is ",end='')
        game = input()
        if game == '1':
            add1()        

        elif game == '3':
            add3()
        else:
            continue
        
        print("Try again? Y/N")
        status = input().upper()
        if status == "Y":
            pass
        elif status == "N":
            print("End game!!")
            print("Thank you for your play!!")
            break
        else:
            continue

sys2Game()
