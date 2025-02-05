
def main():
    sum = 0
    matrix1 = [[5, 10], 
               [2, 3]]
    
    matrix2 = [[4, 12], 
               [5, 2]]
    
    result = [[0, 0], 
              [0, 0]]
    
    """ 
    This is a brute force solution to visualize what operations must be done

    TODO Allow user to enter data for both matricies manually.
    Ensure the input is valid I.E. the number of columns of the first matrix match
    the number of rows of the second matrix. 

    TODO Possible solution for finding the product matrix could be to rotate the
    second matrix in a separate helper function, then iterating through and 
    finding the resulting matrix's values could be more feasable.

    TODO Ensure the resulting matrix is displayed like an actual matrix, 
    instead of lists (remove the commas).
    """


    result[0][0] = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]

    result[0][1] = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]

    result[1][0] = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]

    result[1][1] = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]

    for row in range(len(result)):
        print(result[row])

main()