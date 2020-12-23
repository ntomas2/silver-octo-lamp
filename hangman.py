# Write your code here
import random
from string import ascii_lowercase

list_of_words = ['python', 'java', 'kotlin', 'javascript']
while True:
    user_input = input('Type "play" to play the game, "exit" to quit: ')
    if user_input == 'exit':
        break
    elif user_input != 'play':
        continue
    else:
        hidden_word = random.choice(list_of_words)
        hint = list('-' * len(hidden_word))
        wrong_answers = set()
        attempts = 8
        print('H A N G M A N')
        while attempts > 0:
            print()
            if hint == list(hidden_word):  # Блок выхода из цикла при угадывании слова
                print(hidden_word)
                print('You guessed the word!')
                print('You survived!')
                break
            print(''.join(hint))
            user_input = input('Input a letter: ')
            if len(user_input) != 1:  # проверка на количество символов
                print('You should input a single letter')
                continue
            else:
                if user_input in ascii_lowercase:
                    if user_input in hidden_word:
                        if user_input not in hint:  # проверка на повторении символа
                            for i in range(len(hidden_word)):
                                if user_input == hidden_word[i]:
                                    hint[i] = hidden_word[i]
                        else:
                            print("You've already guessed this letter")
                    else:
                        if user_input not in wrong_answers:
                            wrong_answers.add(user_input)
                            print("That letter doesn't appear in the word")
                            attempts -= 1
                        else:
                            print("You've already guessed this letter")
                else:
                    print('Please enter a lowercase English letter')
                    continue
        else:
            print('You lost!')
            print()
            continue

