# write your code here
board = [' ' for _ in range(0, 10)]
board = [list(board[0:3]), list(board[3:6]), list(board[6:9])]
step_counter = 1
print("---------")
print("|", " ".join(board[0]), "|")
print("|", " ".join(board[1]), "|")
print("|", " ".join(board[2]), "|")
print("---------")
while True:
    coordinates = [number for number in input('Enter the coordinates: ').split()]
    if coordinates[0] not in '0123456789' or coordinates[1] not in '0123456789':
        print('You should enter numbers!')
        continue
    else:
        if int(coordinates[0]) not in range(1, 4) or int(coordinates[1]) not in range(1, 4):
            print('Coordinates should be from 1 to 3')
            continue
        if board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == ' ':
            if step_counter % 2 != 0:
                board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'X'
                print("---------")
                print("|", " ".join(board[0]), "|")
                print("|", " ".join(board[1]), "|")
                print("|", " ".join(board[2]), "|")
                print("---------")
                step_counter += 1
                win_conditions = [board[0].count('X') == 3 or board[0].count('O') == 3,
                                  board[1].count('X') == 3 or board[1].count('O') == 3,
                                  board[2].count('X') == 3 or board[2].count('O') == 3,
                                  board[0][0] == board[1][0] == board[2][0] == 'X',
                                  board[0][0] == board[1][0] == board[2][0] == 'O',
                                  board[0][1] == board[1][1] == board[2][1] == 'X',
                                  board[0][1] == board[1][1] == board[2][1] == 'O',
                                  board[0][2] == board[1][2] == board[2][2] == 'X',
                                  board[0][2] == board[1][2] == board[2][2] == 'O',
                                  board[0][0] == board[1][1] == board[2][2] == 'X',
                                  board[0][0] == board[1][1] == board[2][2] == 'O',
                                  board[0][2] == board[1][1] == board[2][0] == 'X',
                                  board[0][2] == board[1][1] == board[2][0] == 'O']
                if any(win_conditions):
                    print('X wins')
                    break
                elif step_counter == 10:
                    print('Draw')
                    break
            else:
                board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'O'
                print("---------")
                print("|", " ".join(board[0]), "|")
                print("|", " ".join(board[1]), "|")
                print("|", " ".join(board[2]), "|")
                print("---------")
                step_counter += 1
                win_conditions = [board[0].count('X') == 3 or board[0].count('O') == 3,
                                  board[1].count('X') == 3 or board[1].count('O') == 3,
                                  board[2].count('X') == 3 or board[2].count('O') == 3,
                                  board[0][0] == board[1][0] == board[2][0] == 'X',
                                  board[0][0] == board[1][0] == board[2][0] == 'O',
                                  board[0][1] == board[1][1] == board[2][1] == 'X',
                                  board[0][1] == board[1][1] == board[2][1] == 'O',
                                  board[0][2] == board[1][2] == board[2][2] == 'X',
                                  board[0][2] == board[1][2] == board[2][2] == 'O',
                                  board[0][0] == board[1][1] == board[2][2] == 'X',
                                  board[0][0] == board[1][1] == board[2][2] == 'O',
                                  board[0][2] == board[1][1] == board[2][0] == 'X',
                                  board[0][2] == board[1][1] == board[2][0] == 'O']
                if any(win_conditions):
                    print('O wins')
                    break
        else:
            print('This cell is occupied! Choose another one!')
            continue
