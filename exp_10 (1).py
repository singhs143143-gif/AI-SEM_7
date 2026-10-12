def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):

    if row == n:
        print_board(board, n)
        return True

    found = False

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row] = col

            if solve_n_queens(board, row + 1, n):
                found = True

            board[row] = -1

    return found

def print_board(board, n):
    print("\nSolution:")
    for row in range(n):
        for col in range(n):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Main program
n = int(input("Enter number of queens: "))
board = [-1] * n
if not solve_n_queens(board, 0, n):
    print("No solution exists.")