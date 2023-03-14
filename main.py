from board import Board
from symbols import Symbols


def main():
    board = Board()

    print(board)

    print("Player 1, please enter your move")

    board.move(Symbols.Cross, 0, 2)

    print(board)
    print(board.running)
    board.move(Symbols.Cross, 0, 1)
    print(board)
    print(board.running)
    board.move(Symbols.Cross, 0, 0)

    print(board)
    print(board.running)


if __name__ == '__main__':
    main()
