import random

loweralpha = 'abcdefghijklmnopqrstuvwxyz'
upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
spc = '!@#$%&?'

def printPass(pswd):
    random.shuffle(pswd)
    print('Here is your password:', ''.join(pswd))

def easy():
    n = random.randint(6, 8)
    pswd  = random.choices(loweralpha, k = n)
    if random.choice([True, False]):
        ind = random.randint(0, n-1)
        pswd[ind] = random.choice(upperalpha)
    printPass(pswd)

def medium():
    len = random.randint(8, 12)
    spcnum = random.randint(1, 2)
    numnum = random.randint(1, 2)
    upnum = random.randint(1, 3)
    pswd = random.choices(spc, k = spcnum) + random.choices(num, k = numnum) + random.choices(upperalpha, k = upnum) + random.choices(loweralpha, k = len - spcnum - upnum - numnum)
    printPass(pswd)

# def hard():
#     len = random.randint(12, 16)
#     pswd = [
#         random.choice(upperalpha),
#         random.choice(upperalpha),
#         random.choice(num),
#         random.choice(num),
#         random.choice(spc),
#         random.choice(spc)
#     ]
#     pswd += random.choices(loweralpha + upperalpha + num + spc, k = len - len(pswd))
#     random.shuffle(pswd)
#     print(f"Hard Password: {''.join(pswd)}")

print("What type of password would you like?")
print("1. Easy - 6 to 8 characters, only letters (optional uppercase)")
print("2. Medium - 8 to 12 characters, at least 1 uppercase, 1 number, and 1 special character")
print("3. Hard - 12 to 16 characters, at least 1 uppercase, 2 numbers, and 2 special characters")

ch = int(input('Enter your choice (1/2/3): '))
if ch == 1:
    easy()
elif ch == 2:
    medium()
# elif ch == 3:
#     hard()
else:
    print('Invalid input.')