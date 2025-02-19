import random
flag = True
while flag:
    roll = random.randint(1, 6)
    print('You have rolled a', roll)
    ip = input('Do you want to continue? (Y/N): ')
    if ip.upper() == 'N':
        flag = False