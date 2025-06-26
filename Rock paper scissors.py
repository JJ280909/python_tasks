import random

comp_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('rock, paper or scissors? ' )

if user_choice == comp_choice:
    print('TIE')
elif user_choice == 'paper' and comp_choice == 'scissors':
    print('computer wins')
elif user_choice == 'paper' and comp_choice == 'rock':
    print('user wins')
elif user_choice == 'rock' and comp_choice == 'scissors':
    print('user wins')
elif user_choice == 'rock' and comp_choice == 'paper':
    print('computer wins')
elif user_choice == 'scissors' and comp_choice == 'paper':
    print('user wins')
elif user_choice == 'scissors' and comp_choice == 'rock':
    print('computer wins')
else:
    winner = input('please input: rock, paper, scissors')







