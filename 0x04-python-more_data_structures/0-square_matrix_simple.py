#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        A function that returns the square value of all elements in a
        multi dimensional list been passed as arguments.
        Returns a new matrix that is of same size as the size of the
        matrix passed to it as arguments.
        You are allowed to use regular loops, map, etc
    '''
    newlst = []
    if len(matrix) == 0:
        return newlst

    newlst = [[row*row for row in column] for column in matrix]
    return newlst
