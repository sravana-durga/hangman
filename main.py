import symbol
import words
import random
def printing(chance,word):
    for i in range(len(symbol.stages[chance])):
            if i == 2:
                for j in word:
                    print(j,end=' ')
                print(end='\t')
                print(symbol.stages[chance][i],end='\n')
            else:
                for j in word:
                    print(' ',end=' ')
                print(end='\t')
                print(symbol.stages[chance][i],end='\n')
def hangman(option):
    word = random.choice(words.list_of_words[option])
    lives = 0
    display = [ ' ' if i == ' ' else '_' for i in word]
    printing(lives,display)
    while lives<7:
        letter = input('Enter an alphabet:').lower()
        if not('a'<=letter<='z'):
            print('Enter a valid alphabet')
        else:
            
            if letter in display:
                print('You already entered this alphabet, try again')
                printing(lives,display)
            elif letter in word:
                for position in range(len(word)):
                    if word[position]==letter:
                        display[position] = letter
                printing(lives,display)
                if '_' not in display:
                    print('You Guessed the word!')
                    print('Congrats! You won')
                    break
            else:
                print('This alphabet is not there in this word!')
                lives+=1
                printing(lives,display)
    else:
        print('Sorry! You did not guess the word!' )
        print('Computer won')
             

def game():
    print('Rules:')
    print('''
--> Select one topic from the list of topics given
--> In this game, you need to guess the correct word and to guess the word you have 7 chances.
--> Enter a character, if the character is present in the word, then you will not loose the chance.
--> Each and every time when you guess a wrong character, a chance will be lost.
--> If you guess the word correctly before loosing all the chances you will win, else computer will win.
''')
    while True:
        
            op = int(input('''TOPICS:
    1. Python Keywords
    2. Countries
    3. Languages
    Enter your option:'''))
            if op in (1,2,3):
                hangman(op)
            else:
                print('Please enter a valid option!')
            option = input('Want to try again(y/n):')
            if option.upper() == 'Y':
                continue
            else:
                print('Thank You!')
                break
        
if __name__ == '__main__':
    print(symbol.logo)
    print('-----------------------------WELCOME-------------------------------')
    print()
    game()

    