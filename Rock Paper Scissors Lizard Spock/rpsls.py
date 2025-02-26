import random

def getChoice():
    choices = ['r','p','s','l','o']
    ind = random.randint(0, 4)
    return choices[ind]

def sameChoice():
    sen = ['Ah! A battle of twins! No winner this time.',
           'Great minds think alike... but also get stuck in a loop.',
           'The same choice! The universe is in perfect balance.']
    ind = random.randint(0, 3)
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
winning_cases = {
    'r': ['s', 'l'],
    'p': ['r', 'o'],
    's': ['p', 'l'],
    'l': ['o', 'p'],
    'o': ['r', 's'] }

print('----- Rock Paper Scissors Lizard Spock -----')
print('1. Rock crushes Scissors')
print('2. Paper covers Rock')
print('3. Scissors cuts Paper')
print('4. Rock crushes Lizard')
print('5. Lizard eats Paper')
print('6. Paper disproves Spock')
print('7. Spock smashes Scissors')
print('8. Scissors decapitates Lizard')
print('9. Lizard poisons Spock')
print('10. Spock vaporizes Rock\n')

while flag:
    uch = input('Enter your choice (r/p/s/l/o): ').lower()
    cch = getChoice()

    if uch in winning_cases:
        if uch == cch:
            sameChoice()
        elif cch in winning_cases[uch]:
            userWin()
        else:
            compWin()
    else:
        wrongInput()
    play = input('\nWant to continue playing? (y/n): ')
    if play.lower() == 'n':
        flag = False

print('----- Nice game! -----\n')