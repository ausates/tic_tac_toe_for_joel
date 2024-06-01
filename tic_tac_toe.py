import random

board = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "i"
}

def display_board(board):
    row1 = ["a", "b", "c"]
    row2 = ["d", "e", "f"]
    row3 = ["g", "h", "i"]
    rows = [row1, row2, row3]
    for row in rows:
        print(f"{board[row[0]]}|{board[row[1]]}|{board[row[2]]}")


def validate_input(input):
    valid_positions = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    if input not in valid_positions:
        raise Exception("bad input")
    else:
        return True


def get_player_positional_input() -> str:
    player_input = input("Enter a position from the board that you'd like to go: ")
    try:
        validate_input(player_input.lower())
    except Exception as e:
        print(e)
        get_player_positional_input()
    
    return player_input


def computer_input(board):
    not_filled_space_arr = []
    for i in board:
        if board[i] != "X":
            not_filled_space_arr.append(i)
    position = random.randint(0, (len(not_filled_space_arr)-1))
    position = not_filled_space_arr[position]
    print(position)
    return position  # this should be a letter

def test_win(board):
    wins = [["a", "b", "c"], ["a", "d", "g"], ["a", "e", "i"], ["b", "e", "h"], ["c", "f", "i"], ["c", "e", "g"], ["d", "e", "f"], ["g", "h", "i"]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]]:
            print(f"Winner: {win[0]}, {win}")
            return True
    return False


def increment_plays(moves: int) -> int:
    return moves + 1

def tic_tac_toe():
    while not test_win(board=board):
        display_board(board=board)
        print("You will be Xs")
        player_position = get_player_positional_input()
        board[player_position] = "X"
        board[computer_input(board)] = "O"


tic_tac_toe()
