import random
ans = random.randint(1,100)
guesses = [0]

def printGuessTip(num, guesses):
    # 拿當前的猜測數字跟前一次猜測數字作比較較接近顯示 WARMER, 叫遠離顯示COLDER
    # 如果這是第一次猜測, 根據第一次猜測給予提示往上猜或是往下猜
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('你猜測的數字比上一次猜測更接近了')
        elif abs(num-guess) == abs(num-guesses[-2]):
            print('Try different guess')
        else:
            print('COLDER than previous guess!!')
    else:
        if num-guess > 0:
            print('try higher number!')
        else:
            print('try lower number!')


while True:

    # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    # here we compare the player's guess to our number
    if guess == ans:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
        
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    # if guesses[-2]:  
    #     if abs(num-guess) < abs(num-guesses[-2]):
    #         print('WARMER!')
    #     else:
    #         print('COLDER!')
   
    # else:
    #     if num-guess > 0:
    #         print('Guess higher!')
    #     else:
    #         print('Guess lower!')

    printGuessTip(ans, guesses)
