# time complexity O(n**2)
# space complexity O(n)

def rotate(matrix):
    # TODO
    n = len(matrix)
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse the rows
    for i in range(n):
        matrix[i].reverse()
    return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))



'''
a-0-0 = a-2-0
a-0-1 = a-1-0
a-0-2 = a-0-0
a-1-0 = a-2-1
a-1-1 = a-1-1
a-1-2 = a-0-1
a-2-0 = a-2-2
a-2-1 = a-1-2
a-2-2 = a-0-2
'''