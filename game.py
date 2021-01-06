# Write your code here
import random

user_name = input('Enter your name: ')
print(f'Hello, {user_name}')
options = input().split(',')
print("Okay, let's start")
win_conditions = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
if len(options) > 1:
    correct_input = ['!exit', '!rating'] + options
else:
    correct_input = ['!exit', '!rating', 'paper', 'scissors', 'rock']
    options = ['paper', 'scissors', 'rock']
file_name = 'rating.txt'
file = open(file_name, 'r')
text = [line.replace('\n', '') for line in file.readlines()]
rates = {}
for line in text:
    s = line.split()
    rates[s[0]] = int(s[1])
if user_name not in rates.keys():
    rates[user_name] = 0
file.close()
while True:
    user_choice = input()
    computer_choice = random.choice(options)
    varieties = {'lose': f'Sorry, but the computer chose {computer_choice}',
                 'draw': f'There is a draw ({computer_choice})',
                 'win': f'Well done. The computer chose {computer_choice} and failed'}
    if user_choice in correct_input:
        if user_choice != '!exit' and user_choice != '!rating':
            if user_choice == computer_choice:
                print(varieties['draw'])
                rates[user_name] += 50
            elif computer_choice in win_conditions[user_choice]:
                print(varieties['win'])
                rates[user_name] += 100
            else:
                print(varieties['lose'])
        else:
            if user_choice == '!exit':
                print('Bye!')
                break
            else:
                print(f'Your rating: {rates[user_name]}')
    else:
        print('Invalid input')
