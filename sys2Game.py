import random
import time

ans = None
too_slow = False

def gen_digit():
    #genDigit() used to create number
    #that have 4 digit in gameplay.
    digit = ''
    while len(digit) != 4:
        num = random.randint(0,9)
        num = str(num)
        digit += num
    return digit


def plus_1(digit):
    #for generate answer of this game
    #by plus 1 for every number in 4 digits.
    new_digit = ''
    for l in digit:
        l = int(l)
        l += 1
        if l == 10: #we expect 0 for an answer if number is 9.
            l = 0
        l = str(l)
        new_digit += l
    return new_digit
   
def plus_3(digit):
    #for generate answer of this game
    #by plus 3 for every number in 4 digits.
    new_digit = ''
    for l in digit:
        l = int(l)
        l += 3
        if l >= 10: 
            l %= 10
            #if value of digit + 3 is between 10 and 12,
            #we expect a answer for value - 10.  
        l = str(l)
        new_digit += l
    return new_digit
    


def game_over():
    print("Game over!!")
    print("the correct answer is " + digit_ans + ".") #show the right anwer.
    print("Your longest streak is " + str(streak) + '.')
    #show streak that player has done in this game.
        
def add_1():
    flag = True
    global streak
    streak = 0 
    while flag:
        digit = gen_digit()
        print(digit)
        #prepare the number that have 4 digit for this game.
        global digit_ans
        digit_ans = plus_1(digit) #use plus_1 to prepare the answer.
        ans = input("Input your here: ") #recieve answer from player.
        if ans == digit_ans: #when player input the correct answer.
            print("Correct!!") #tell them that they input a right anwer.
            streak += 1  #and give they a streak.           
        else:
            game_over() #show result that they do in this game
            flag = False #for any input that incorrect and end this function.
            
            
        
def add_3():
    flag = True
    global streak
    streak = 0 
    while flag:
        digit = gen_digit()
        print(digit)
        #prepare the number that have 4 digit for this game.
        global digit_ans
        digit_ans = plus_3(digit) #use plus_1 to prepare the answer.
        ans = input("Input your here: ") #recieve answer from player.
        if ans == digit_ans: #when player input the correct answer.
            print("Correct!!") #tell them that they input a right anwer.
            streak += 1  #and give they a streak.           
        else:
            game_over() #show result that they do in this game
            flag = False #for any input that incorrect and end this function.
        
def sys_2_game():
    while True:
        print("Welcome!!")
        print("Choose Your challenge.")
        print("Press 1 to choose add_1")
        print("Press 3 to choose add_3")
        print("Your choice is ",end='')
        #print welcome message
        #and tell player that they have to choose level in this game.
        game = input()
        if game == '1':
            add_1()
        elif game == '3':
            add_3()
        else:
            continue        
        print("Try again? Y/N")
        #when player end game by they in correct answer.
        #ask them that will they continue this game?
        status = input().upper()
        if status == "Y":
            pass
        elif status == "N":
            print("End game!!")
            print("Thank you for playing!!") #goodbye message
            break
        else:
            print("For next time please give we a input of 'Y' or 'N'")
            print("Thank you for playing!!") 
            break

sys_2_game()
