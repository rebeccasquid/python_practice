import random
ans = random.randint(1,100)
guesses = [0]


# 隨機生成一個解答
# 提醒使用者輸入一個合法數字
# 如果使用者輸入不合法數字 => 請他重新輸入合法數字
# 如果使用者輸入合法的數字 => 拿使用者猜測數字與隨機生成解答進行比較

# 根據使用者猜測數字與隨機生成解答 提供提示給使用者
# - 猜測的數字比上一次猜測距離正確答案”更接近“了呢'
# - 你猜測的數字比上一次猜測距離正確答案”是一樣的
# - 你猜測的數字比上一次猜測距離正確答案“更遠”了呢
# - 正確答案你比猜測的數字大
# - 正確答案你比猜測的數字小


def printGuessTip(num, guesses):
    # 拿當前的猜測數字跟前一次猜測數字作比較較接近顯示 WARMER, 叫遠離顯示COLDER
    # 如果這是第一次猜測, 根據第一次猜測給予提示往上猜或是往下猜
    if len(guesses)>=2 and guesses[-2]:  
        if abs(num-guesses[-1]) < abs(num-guesses[-2]):
            print('你猜測的數字比上一次猜測距離正確答案”更接近“了呢')
        elif abs(num-guesses[-1]) == abs(num-guesses[-2]):
            print('你猜測的數字比上一次猜測距離正確答案”是一樣的“')
        else:
            print('你猜測的數字比上一次猜測距離正確答案“更遠”了呢')
    else:
        if num-guesses[-1] > 0:
            print('正確答案你比猜測的數字大')
        else:
            print('正確答案你比猜測的數字小')

# printGuessTip(10,[8])

while True:

    # make sure input is a valid number
    inputText = input("I'm thinking of a number between 1 and 100.\n  What is your guess? ")
    if str.isdigit(inputText) == False :
        print('Please try the valid integer ')
        continue

    # we can copy the code from above to take an input
    guess = int(inputText)
    
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
