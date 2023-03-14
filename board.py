from symbols import Symbols

triple_equals = [
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
        self.__fields[row][column] = player

        self.running = self.__check_game_state()

    def __check_game_state(self):
        for triple_equal in triple_equals:
            if self.__check_triple_equal(triple_equal):
                return True

        return False

    def __check_triple_equal(self, triple_equals_tuple):
        first_tuple = triple_equals_tuple[0]
        second_tuple = triple_equals_tuple[1]
        third_tuple = triple_equals_tuple[2]
        return Board.__triple_equals(self.__fields[first_tuple[0]][first_tuple[1]],
                                     self.__fields[second_tuple[0]][second_tuple[1]],
                                     self.__fields[third_tuple[0]][third_tuple[1]])

    @staticmethod
    def __triple_equals(first, second, third):
        return first != Symbols.Empty and first == second and second == third
