from square_filled_error import SquareFilledError
from symbols import Symbols

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


class Board:
    def __init__(self):
        self.__fields = [[Symbols.Empty for i in range(3)] for j in range(3)]
        self.running = True

    def __str__(self):
        output = "-" * 13 + "\n"
        for row in self.__fields:
            output += "|"
            for column in row:
                output += f" {column.value} |"
            output += "\n" + "-" * 13 + "\n"

        return output

    def move(self, player, row, column):
        if self.__fields[row][column] != Symbols.Empty:
            raise SquareFilledError

        self.__fields[row][column] = player
        self.running = not self.__is_game_finished()

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
        return Board.__triple_equals(
            self.__fields[position1_row][position1_column],
            self.__fields[position2_row][position2_column],
            self.__fields[position3_row][position3_column]
        )

    @staticmethod
    def __triple_equals(first, second, third):
        return first != Symbols.Empty and first == second and second == third
