"""
37. Sudoku Solver
Hard

https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


Example 1:


Input: board = [["5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9"]]
Output: [["5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
Accepted    Submissions
258,961     527,866

"""


from heapq import *
from pprint import pp
from functools import reduce
import operator

MAIN = '__main__'
NUMBERS = set(str(x) for x in range(1, 10))
BLANK = '.'
NOT_BLANK = lambda x: x != BLANK
IS_BLANK = lambda x: x == BLANK
IS_A_NUMBER = lambda x: x in NUMBERS
BLOCK_ZERO = [[(row, col) for row in range(3)] for col in range(3)]
BOARD = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]


# noinspection PyShadowingNames
def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def add_points(p, ps):
    return [add(p, q) for q in ps]


# noinspection PyShadowingNames
def add_block(p, block):
    return list(map(lambda x: add_points(p, x), block))


def div(p, k):
    return p[0] // k, p[1] // k

def mult(p, k):
    return p[0] * k, p[1] * k

def flatten(block):
    return reduce(operator.add, block)

def translate(block_num, block):
    print(f'num = {block_num}, block = {block}')
    size = len(block)
    print(f'size = {size}')
    translation = mult(block_num, size)
    translated = add_block(translation, block)
    print(f'translated = {translated}')
    return translated



# noinspection PyShadowingNames
class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.board = {
                            (i, j): value
                            for i, row in enumerate(matrix)
                            for j, value in enumerate(row)
                      }
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.size = self.height, self.width
        self.rows = [
                        [(row, col) for col in range(self.width)]
                        for row in range(self.height)
                    ]
        self.cols = [
                        [(row, col) for row in range(self.height)]
                        for col in range(self.width)
                    ]
        self.fixed = {
                            point: value
                            for point, value in self.board.items()
                            if value in NUMBERS
                     }
        self.remaining = {
                            point: self.get_moves(point)
                            for point, value in self.board.items()
                            if value == BLANK
                         }
        self.played = dict()

    def get_board(self):
        return self.board

    def get_remaining(self):
        return self.remaining

    def get_value(self, point):
        return self.board[point]

    def set_value(self, point, value):
        self.board[point] = value

    def make_move(self, move):
        point, value = move
        self.set_value(point, value)

    @staticmethod
    def get_block(point):
        block_num = div(point, 3)
        return translate(block_num, BLOCK_ZERO)

    def get_block_nums(self, point):
        return set(
                    filter(
                            NOT_BLANK,
                            map(
                                self.get_value, flatten(Board.get_block(point))
                               )
                          )
                  )

    def get_row_nums(self, point):
        return set(
                    filter(
                            NOT_BLANK,
                            map(
                                self.get_value, self.rows[point[0]]
                               )
                           )
                  )

    def get_col_nums(self, point):
        return set(
                    filter(
                            NOT_BLANK,
                            map(
                                self.get_value, self.cols[point[1]]
                               )
                           )
                  )

    def get_unplayable(self, point):
        r_nums = self.get_row_nums(point)
        c_nums = self.get_col_nums(point)
        b_nums = self.get_block_nums(point)
        return r_nums | c_nums | b_nums

    def get_moves(self, point):
        return NUMBERS - self.get_unplayable(point)


# noinspection PyShadowingNames
class Play:
    def __init__(self, board):
        self.board = board

    def update_played(self, move):
        point, num = move
        self.played[point] = num

    def get_next_play(self):
        moves = self.board.get_remaining()
        return min(rem, key=lambda point: len(moves[point]))

    def play(self, move):
        board = self.board
        board.make_move(move)
        point, value = move
        board.played[point] = value
        row, col = point
        rows, cols = board.rows[row], board.cols[col]
        block = flatten(board.get_block((row, col)))
        affected = rows + cols + block
        for point in affected:











# noinspection PyShadowingNames
def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    pass


if __name__ == MAIN:
    # noinspection PyShadowingBuiltins
    board = [
                ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']
            ]

    b = Board(BOARD)
    # pp(b.fixed)
    #
    p = (2, 3)
    r_nums = b.get_row_nums(p)
    c_nums = b.get_col_nums(p)
    print(f'p = {p}')
    b_nums = b.get_block_nums(p)
    print(f'p = {p}')
    moves = b.get_moves(p)
    print(f'r_nums = {r_nums}')
    print(f'c_nums = {c_nums}')
    print(f'b_nums = {b_nums}')
    print(f'moves = {moves}')

    # print(min([1, 1, 2, 3, 5]))
    #
    # d = {320: '12', 321: '032', 322: '3'}
    # print(f'min = {min(d, key=lambda y: len(d[y]))}')
    #
    # brd = [
    #     [(row, col) for col in range(3)]
    #     for row in range(2)
    # ]
    #
    # pp(brd)