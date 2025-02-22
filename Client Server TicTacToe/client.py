import socket

s = socket.socket()         
port = 8080               

try:
    s.connect(('localhost', port))
        
    flag = True
    turn = 0

    while flag:
        board = s.recv(1024).decode().replace('[','').replace(']','').replace("'",'').split(',')
        board = [cell.strip() for cell in board]
        
        for i in range(9):
            if i % 3 == 0:
                print()
            print(board[i], end=' ')
        print()

        if turn == 0:
            print("--- Player 1's turn ---")
            ind = input("Enter cell number (0-8): ")
            turn = 1

            s.send(ind.encode())
            res = s.recv(1024).decode()
            while res == '-1':
                ind = input("Enter another cell number (0-8): ")
                s.send(ind.encode())
                res = s.recv(1024).decode()

            if res == 'Player 1 wins':
                print('Player 1 wins')
                flag = False
        else:
            print("--- Player 2's turn ---")
            ind = input("Enter cell number (0-8): ")
            turn = 0

            s.send(ind.encode())
            res = s.recv(1024).decode()
            while res == '-1':
                ind = input("Enter another cell number (0-8): ")
                s.send(ind.encode())
                res = s.recv(1024).decode()

            if res == 'Player 2 wins':
                print('Player 2 wins')
                flag = False

except Exception as e:
    exit()

finally:
    s.close()