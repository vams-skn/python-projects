def checkWin(board, ch):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(8):
        if board[wins[i][0]] == board[wins[i][1]] == board[wins[i][2]] == ch: 
            return False
    return True

def checkEmpty(ind):
    if board[ind] == '-':
        return True
    return False

def printBoard(board):
    for i in range(9):
        if i%3 == 0:
            print()
        print(board[i], end=' ')
    print('\n')

board = ['-','-','-','-','-','-','-','-','-']
count, turn = 0, 0
flag = True
valid = [0,1,2,3,4,5,6,7,8]

while(flag):
    printBoard(board)
    if count == 9:
        print("Tie. No winner.")
        break
    if turn == 0:
        print("--- Player 1's turn ---")
        
        ind = int(input("Enter cell number: "))
        if ind not in valid or not checkEmpty(ind):
            while turn == 0:
                print('Cell invalid or occupied')
                ind = int(input("Enter another cell number: "))
                if checkEmpty(ind):
                    turn = 1
                    board[ind] = 'X'

        turn = 1
        board[ind] = 'X'
        count += 1

        if count > 4:
            flag = checkWin(board, 'X')
            if not flag:
                printBoard(board)
                print('Player 1 wins!')
    else:
        print("--- Player 2's turn ---")
        
        ind = int(input("Enter cell number: "))
        if ind not in valid or not checkEmpty(ind):
            while turn == 1:
                print('Cell invalid or occupied')
                ind = int(input("Enter another cell number: "))
                if checkEmpty(ind):
                    turn = 0
                    board[ind] = 'O'

        turn = 0
        board[ind] = 'O'
        count += 1
        
        if count > 4:
            flag = checkWin(board, 'O')
            if not flag:
                printBoard(board)
                print('Player 2 wins!')