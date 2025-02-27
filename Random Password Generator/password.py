import random

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
spc = '!@#$%&?'

def easy():
    n = random.randint(6, 8)
    pswd = ''
    for i in range(n):
        pswd += random.choice(alpha)
        print(pswd)

easy()