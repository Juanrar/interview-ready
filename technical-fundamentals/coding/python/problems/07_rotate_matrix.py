# 7. *Rotate Matrix*:

# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Matrix = list[list[int]]


def rotate_matrix(matrix: Matrix) -> None:
    pass


# Tests


def test_rotates_2x2_matrix_clockwise():
    matrix = [
        [1, 2],
        [3, 4],
    ]
    rotate_matrix(matrix)
    assert matrix == [
        [3, 1],
        [4, 2],
    ]


def test_rotates_3x3_matrix_clockwise():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_matrix(matrix)
    assert matrix == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]


def test_rotates_4x4_matrix_clockwise():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    rotate_matrix(matrix)
    assert matrix == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]


def test_rotates_5x5_matrix_clockwise():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    rotate_matrix(matrix)
    assert matrix == [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]
