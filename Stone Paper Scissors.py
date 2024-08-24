import random as r

points = 0
while True:
    choice = int(input('''Stone = 1   Paper = 2   Scissors = 3   0 to Quit:
Enter your choice: '''))
    if choice == 0:
        break
    if choice > 3:
        print('Choose between 1 and 3')
        raise ValueError
    ran = r.randint(1, 3) 
    # t = 'Stone' if ran == 1 else t = 'Paper' if ran == 2 else t = 'Scissors'
    if ran == 1:
        t = 'Stone'
    if ran == 2:
        t = 'Paper'
    if ran == 3:
        t = 'Scissors'
    print('The computer choose', t)
    if choice == ran:
        points += 0
        print('Match Draw\n')
    # if choice != r.randint(1, 3):
    else:
        if choice == 1 and ran == 2:
            points = points - 1
            print('Defeat\n')
        if choice == 1 and ran == 3:
            points = points + 1
            print('Victory\n')
        if choice == 2 and ran == 1:
            points = points + 1
            print('Victory\n')
        if choice == 2 and ran == 3:
            points = points - 1
            print('Defeat\n')
        if choice == 3 and ran == 1:
            points = points - 1
            print('Defeat\n')
        if choice == 3 and ran == 2:
            points = points + 1
            print('Victory\n')

if points == 0:
    print('Match Drawn')
if points > 0:
    print(f'Match Won by {points} points')
if points < 0:
    points = points*(-1)
    print(f'Match lost by {points} points')
