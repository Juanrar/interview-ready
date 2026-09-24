# 8. *Zero Matrix*:

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Matrix = list[list[int]]


def zero_matrix(matrix: Matrix) -> None:
    pass


# Tests


def test_zeroes_2x2_matrix():
    matrix = [
        [0, 2],
        [3, 4],
    ]
    zero_matrix(matrix)
    assert matrix == [
        [0, 0],
        [0, 4],
    ]


def test_zeroes_3x3_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 9],
    ]
    zero_matrix(matrix)
    assert matrix == [
        [1, 0, 3],
        [4, 0, 6],
        [0, 0, 0],
    ]


def test_zeroes_4x4_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    zero_matrix(matrix)
    assert matrix == [
        [1, 2, 0, 4],
        [0, 0, 0, 0],
        [9, 10, 0, 12],
        [13, 14, 0, 16],
    ]


def test_two_zeroes_4x4_matrix():
    matrix = [
        [0, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    zero_matrix(matrix)
    assert matrix == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 10, 0, 12],
        [0, 14, 0, 16],
    ]
