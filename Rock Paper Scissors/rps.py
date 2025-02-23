import random

def getChoice():
    choices = ['r','p','s']
    ind = random.randint(0, 2)
    return choices[ind]

def sameChoice():
    sen = ['Ah! A battle of twins! No winner this time.',
           'Great minds think alike... but also get stuck in a loop.',
           'The same choice! The universe is in perfect balance.']
    ind = random.randint(0, 4)
    print(sen[ind])

def compWin():
    sen = ['Oof! The machine prevails this time.',
           'Better luck next time, human.',
           "Defeat stings, doesn't it? The computer smirks.",
           'Your defeat has been recorded in the AI archives.',
           'The CPU flexes its circuits in victory!']
    ind = random.randint(0, 4)
    print(sen[ind])  

def userWin():
    sen = ['Boom! Victory is yours. Bow before the champion!',
           'You came, you saw, you conquered! GG.',
           'Nice one! You outsmarted me this time.',
           'You win! The computer is now reevaluating its strategies.',
           'Well played, human. The machines shall remember this loss.']
    ind = random.randint(0, 4)
    print(sen[ind])

def wrongInput():
    sen = ['Huh? That is not an option, but nice try!',
           'Glitch in the matrix detected. Try again.',
           'Are you inventing a new move? Stick to r/p/s!',
           "Nice creativity, but let's keep it to rock, paper, or scissors!",
           'Whoa, are you trying to break the game? Enter r, p, or s!']
    ind = random.randint(0, 4)
    print(sen[ind])

flag = True

print('----- Rock Paper Scissors -----')
print('1. Rock beats Scissors')
print('2. Paper beats Rock')
print('3. Scissors beats Paper\n')

while flag:
    uch = input('Enter your choice (r/p/s): ')
    cch = getChoice()
    if uch.lower() == 'r':
        if cch == 'r':
            sameChoice()
        elif cch == 'p':
            compWin()
        else:
            userWin()
    elif uch.lower() == 'p':
        if cch == 'p':
            sameChoice()
        elif cch == 's':
            compWin()
        else:
            userWin()
    elif uch.lower() == 's':
        if cch == 's':
            sameChoice()
        elif cch == 'r':
            compWin()
        else:
            userWin()
    else:
        wrongInput()
    play = input('Want to continue playing? (y/n): ')
    if play.lower() == 'n':
        flag = False

print('----- Nice game! -----\n')