# Client Server TicTacToe

This is a simple TicTacToe game written in Python using a client-server architecture. The server hosts the game, while a client connects to play. 

This script will print the board at every turn and indicates which player's turn it is. It has input validation to prevent invalid moves and detects and terminates the game in case of a draw or a win.

## Run Locally

1. Run the server script first:

    ```bash
    python server.py
    ```

2. Run the client script:

    Open a second terminals and run client.py

    ```bash
    python client.py
    ```

3. Play

    The script indicates which player's turn it is. Enter your move as a number from 0 to 8, where 0 is the top left cell and 8 is the bottom right cell.

## How It Works

- The server maintains the TicTacToe board and handles turn-based gameplay.
- The clients send their moves to the server.
- The server validates moves, updates the board, and notifies players of the result.
- The game ends when a player wins or the board is full.