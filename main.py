from board import Board
from square_filled_error import SquareFilledError
from symbols import Symbols


def main():
    board = Board()

    while board.running:
        try:
            print("--------------------------------")
            print("Player 1, please select a square")
            x = int(input("x (0/1/2): "))
            assert 0 <= x <= 2
            y = int(input("y (0/1/2): "))
            assert 0 <= y <= 2
            board.move(Symbols.Cross, x, y)
        except AssertionError:
            print("Invalid square, please retry!")
        except SquareFilledError:
            print("Square is already filled, please use another one!")
        else:
            print(board)
            print(board.running)


if __name__ == '__main__':
    main()
