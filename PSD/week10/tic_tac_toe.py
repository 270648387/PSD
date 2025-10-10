def generate_board(board):
    print("\n")
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("---------")
    
    print("\n")

def get_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
        
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    return None

def get_player_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Players will be X and O. Enter numbers 1-9 to make your move.")
    
    board = [" " for _ in range(9)]
    current_player = "X"
    
    while True:
        generate_board(board)

        move = get_player_move(current_player, board)
        board[move] = current_player
        
        # Check for winner
        winner = get_winner(board)
        if winner:
            generate_board(board)
            print(f"Player {winner} wins! Congratulations!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
