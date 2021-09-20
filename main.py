board = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
  # find the next empty sqaure
  find = find_empty(board)
  # if find does not find an empty square, board is compete and returns True
  if not find:
    return True
  else:
    row, col = find
  # iterate through integers 1 to 9 and find if the int is valid
  for i in range(1, 10):
    if valid(board, i, (row, col)):
      board[row][col] = i
      # if int is valid call solve to find the next empty piece
      if solve(board):
        return True
      board[row][col] = 0

  return False


def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print('- - - - - - - - - - - - - - ')
    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print(' | ', end="")
      if j == 8:
        print(board[i][j])
      else:
        print(str(board[i][j]) + ' ', end="")


def find_empty(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i,j)
  return None


def valid(board, num, pos):
  # validate row
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and pos[1] != i:
      return False

  # validate column
  for i in range(len(board)):
    if board[i][pos[1]] == num and pos[0] != i:
      return False

  # validate box
  box_x = pos[1] // 3
  box_y = pos[0] // 3
  for i in range(box_y * 3, box_y * 3 + 3):
    for j in range(box_x * 3, box_x * 3 + 3):
      if board[i][j] == num and (i, j) != pos:
        return False
  return True

# example
print_board(board)
solve(board)
print("   ")
print_board(board)
