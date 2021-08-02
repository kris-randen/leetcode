from board import Board

# noinspection PyShadowingNames
class Point:
    def __init__(self, row, col, board=Board()):
        self.board = board
        self.row = row
        self.col = col
        self.point = (row, col)
        self.moves = dict()

    def get_point(self):
        return self.point

    def get_value(self):
        return self.board.get_value(self)

    def get_block(self):
        block_num = div(self.point, 3)
        return add_points(block_num, BLOCK_ZERO)

    def get_block_nums(self):
        return set(filter(NOT_BLANK, (self.board[row][col] for (row, col) in self.get_block())))

    def get_moves(self):
        row_nums, col_nums = get_nums_i_j(board, *self.point)
        block_nums = self.get_block_nums()
        blocked = set().union(row_nums, col_nums, block_nums)
        return NUMBERS.difference(blocked)

    def __eq__(self, other):
        return len(self.get_moves()) == len(other.get_moves())

    def __lt__(self, other):
        return len(self.get_moves()) < len(other.get_moves())

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return not self < other

    def __gt__(self, other):
        return not self < other and not self == other
