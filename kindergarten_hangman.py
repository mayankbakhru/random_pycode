import random
import string

def print_list(current):
    for i in range(len(current)):
        print (current[i],end = '')
    print()


def guess(chosen,current, wrong_count,wrong_guess):
    
    print ('enter your guess:', end='')
    var = input()
    if len(var) != 1:
        print ('enter only one character.')
        while( len(var) != 1 ):
            print ('enter your guess:', end='')
            var = input()
    var = var.lower()
    indices = [i for i, x in enumerate(chosen) if x == var]
    res_flag = -1
    if len(indices)!=0:
        print ("You guessed right!!")
        for i in range(len(indices)):
            current[indices[i]] = var
        print("You have unlocked new spots:",end='')    
        print_list(current)
        print("Your wrong guesses till now:",end='')    
        print_list(wrong_guess)
        res_flag = 1
    else:
        print ("you guessed wrong :(")       
        
        if var not in wrong_guess:
            wrong_guess.append(var)
            wrong_count = wrong_count+1
        print_hangman(wrong_count)
        print("You have not unlocked any new spots:(")    
        print_list(current)
        print("Your wrong guesses till now:",end='')    
        print_list(wrong_guess)
        res_flag = 0
    return (current,res_flag,wrong_count,wrong_guess)

def start():
    game()
    while(True):
        print ("Do you want to play again?(y/n):", end='')
        x = input()
        if (x.lower()!='y' and x.lower()!='n'):
            while (x.lower()!='y' and x.lower()!='n'):
                print("Invalid input! try again:",end='')
                x = input()
        if (x.lower()=='n'):
            break
        game()

def game():
    # words = ['cute','girl','letter','father','mother','grandfather','family','grandmother']
    words = ['all','am','are','at','ate','be','black','brown','but','came','did','do','eat','four','get','good','have','he','into','like','must','new','no','now','on','our','out','please','pretty','ran','ride','saw','say','she','so','soon','that','there','they','this','too','under','want','was','well','went','what','white','who','will','with','yes']
    choose = random.randint(0,len(words)-1)
    chosen = words[choose]
    current = list()
    wrong_guess = list()
    for i in range(len(chosen)):
        current.append('-')

    print("I have chosen a %d letter word for you." % (len(chosen)))
    print_list(current)
    print ("You get 7 chances to guess letters in that word...")
    wrong_count = 0

    while (wrong_count < 7 ):
        if '-' not in current: 
            break
        result = guess(chosen,current,wrong_count,wrong_guess)
        current = result[0]
        output = result[1]
        wrong_count = result[2]
        wrong_guess = result[3]
        
    if (wrong_count == 7):
        print ("Game Over.... Try again!")
        print ("Answer: "+ chosen)
    else:
        print("Good job!.... you cracked the puzzle")
    return (0)

    
def print_hangman(pos):
    # x = input()
    hangman = ["--",'|','|0','|+',' |','/'," \\"]
    # i = pos
    print("HANGMAN")
    for i in range(pos):
        if (hangman[i]=='/'):
            print(hangman[i],end='')
        else:
            print(hangman[i])
 
if __name__ == "__main__":
    start()
