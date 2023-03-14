from square_filled_error import SquareFilledError
from square_state import SquareState

three_fields_equals_options = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
]


class Game:
    def __init__(self):
        self.running = True
        self.__fields = [[SquareState.Empty for _ in range(3)] for _ in range(3)]
        self.__player_to_move = SquareState.Cross

    def get_board_string(self):
        output = "-" * 13 + "\n"
        for row in self.__fields:
            output += "|"
            for column in row:
                output += f" {column.value} |"
            output += "\n" + "-" * 13 + "\n"

        return output

    def get_player_to_move_string(self):
        return f"Player 1 ({self.__player_to_move.value})" \
            if self.__player_to_move == SquareState.Cross \
            else f"Player 2 ({self.__player_to_move.value})"

    def fill_square(self, row, column):
        if self.__fields[row][column] != SquareState.Empty:
            raise SquareFilledError

        self.__fields[row][column] = self.__player_to_move
        self.running = not self.__is_game_finished()

        if self.running:
            self.__switch_player_to_move()

    def __switch_player_to_move(self):
        self.__player_to_move = SquareState.Cross if self.__player_to_move == SquareState.Circle else SquareState.Circle

    def __is_game_finished(self):
        for option in three_fields_equals_options:
            if self.__check_three_fields_equal(option):
                return True

        return False

    def __check_three_fields_equal(self, three_field_equal_option):
        position1, position2, position3 = three_field_equal_option
        position1_row, position1_column = position1
        position2_row, position2_column = position2
        position3_row, position3_column = position3
        return Game.__triple_equals(
            self.__fields[position1_row][position1_column],
            self.__fields[position2_row][position2_column],
            self.__fields[position3_row][position3_column]
        )

    @staticmethod
    def __triple_equals(first, second, third):
        return first != SquareState.Empty and first == second and second == third
