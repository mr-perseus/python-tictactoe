from game import Game
from square_filled_error import SquareFilledError


def main():
    game = Game()

    while game.running:
        try:
            print(f"{game.get_player_to_move_string()}, please select a square")
            row = int(input("row (0/1/2): "))
            assert 0 <= row <= 2
            col = int(input("col (0/1/2): "))
            assert 0 <= col <= 2
            game.fill_square(row, col)
        except AssertionError:
            print("Invalid square, please retry!")
        except SquareFilledError:
            print("Square is already filled, please use another one!")
        else:
            print(game.get_board_string())

    print(f"The game has finished. The winner is {game.get_player_to_move_string()}")


if __name__ == '__main__':
    main()
