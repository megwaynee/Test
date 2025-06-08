# Simple Tic Tac Toe game for two players

def print_board(board):
    print('\n'.join([' | '.join(row) for row in board]))
    print()


def check_win(board, player):
    # check rows, columns and diagonals
    lines = []
    lines.extend(board)  # rows
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  # cols
    lines.append([board[i][i] for i in range(3)])  # diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # other diagonal
    return any(all(cell == player for cell in line) for line in lines)


def full(board):
    return all(cell != ' ' for row in board for cell in row)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        try:
            move = input(f"Player {player}, enter your move as row,col (1-3): ")
            if move.lower() in ('q', 'quit', 'exit'):
                print('Game aborted.')
                break
            r, c = [int(x) - 1 for x in move.split(',')]
            if not (0 <= r < 3 and 0 <= c < 3) or board[r][c] != ' ':
                print('Invalid move, try again.')
                continue
        except Exception:
            print('Invalid input, use row,col format (e.g., 1,3)')
            continue
        board[r][c] = player
        if check_win(board, player):
            print_board(board)
            print(f'Player {player} wins!')
            break
        if full(board):
            print_board(board)
            print('It\'s a tie!')
            break
        player = 'O' if player == 'X' else 'X'


if __name__ == '__main__':
    tic_tac_toe()
