import socket

host = 'localhost'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)

def checkEmpty(ind):
    if board[ind] == '-':
        return True
    return False

def checkWin(board, ch):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(8):
        if board[wins[i][0]] == board[wins[i][1]] == board[wins[i][2]] == ch:
            return False
    return True

board = ['-','-','-','-','-','-','-','-','-']
count, turn = 0, 0
flag = True
valid = [0,1,2,3,4,5,6,7,8]

try:
    c, add = s.accept()
    print('Socket successfully created')

except:
    print('Error')
    exit()

while flag:
    c.send(str(board).encode())
    if turn == 0:
        ind = int(c.recv(1024).decode())
        if ind not in valid or not checkEmpty(ind):
            while turn == 0:
                c.send('-1'.encode())
                ind = int(c.recv(1024).decode())
                if checkEmpty(ind):
                    turn = 1
                    board[ind] = 'X'

        turn = 1
        board[ind] = 'X'
        count += 1
        c.send('next'.encode())

        if count > 4:
            flag = checkWin(board, 'X')
            if not flag:
                c.send('Player 1 wins'.encode())
                flag = False

    else:
        ind = int(c.recv(1024).decode())
        if ind not in valid or not checkEmpty(ind):
            while turn == 1:
                c.send('-1'.encode())
                ind = int(c.recv(1024).decode())
                if checkEmpty(ind):
                    turn = 0
                    board[ind] = 'O'

        turn = 0
        board[ind] = 'O'
        count += 1
        c.send('next'.encode())

        if count > 4:
            flag = checkWin(board, 'O')
            if not flag:
                c.send('Player 2 wins'.encode())
             
c.close()
s.close()