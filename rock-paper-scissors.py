import random
import json

def update(score, turns):
    try:
        highscoreFile = open('highscore.txt', 'r') #open in read mode
        highscores = json.load(highscoreFile)
        highscoreFile.close()
    except: #if file doesn't exist set highscores to empty list
        highscores = []

    name = input('Enter your name: >')
    newscore = (name, round((score / turns) * 100, 2))
    highscores.append(newscore)

    highscores.sort(key = lambda x: x[1], reverse = True)
    
    for index, highscore in enumerate(highscores):
        print(index + 1, ':', highscore[0], ':', highscore[1],'%')
        
    #save new high score table
    highscoreFile = open('highscore.txt', 'w+') #open in write mode
    json.dump(highscores, highscoreFile)
    highscoreFile.close()

def end():
    print('You scored: ', round((score / turns) * 100, 2), '%')
    update(score, turns)
    raise SystemExit

my_list = ['r', 'p', 's']
turns = 0
score = 0

while True:
    computer_choice = random.choice(my_list)
    my_choice = input('Enter your choice: (r)ock, (p)aper, (s)cissors or \'q\' to quit >')
    #print(my_choice)
    #print(computer_choice)

    if my_choice == 'q':
        end()
    elif my_choice == computer_choice:
        print('Draw')
    elif my_choice == 'r' and computer_choice == 'p' or my_choice == 'p' and computer_choice == 'r' or my_choice == 's' and computer_choice == 'p':
        print('You win!')
        score += 1
    else:
        print('You lose')

    turns += 1
