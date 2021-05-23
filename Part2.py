import math

# each cell is a count of occurs for (i,j) entry in a matrix
# let Y be the rows and X be the columns
example3x3 = [
    [12, 4, 5],
    [4, 11, 6],
    [0, 8, 12]
]
example4x4 = [
    [1 / 8, 1 / 16, 1 / 32, 1 / 32],
    [1 / 16, 1 / 8, 1 / 32, 1 / 32],
    [1 / 16, 1 / 16, 1 / 16, 1 / 16],
    [1 / 4, 0, 0, 0]
]
example5x5 = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9]
]


def convert_to_prob(matrix):
    matrix = [x[:] for x in matrix]
    sum = 0
    for row in matrix:
        for element in row:
            sum += element
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] /= sum
    print(f'p(X=j,Y=i) = c(i,j)/n where n is a total sum of all occurrences, n = {sum}')
    print(f'Result: {matrix}')
    return matrix


def marginal_X(matrix):
    margX = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            margX[j] += matrix[i][j]
    toprint = 'Marginal Distribution of X:\nX - p(X=j)\n'
    for i, elem in enumerate(margX):
        toprint += f'{i} - {round(elem, 3)}\n'
    print(toprint)
    return margX


def marginal_Y(matrix):
    margY = [0] * len(matrix)
    for i in range(len(matrix)):
        margY[i] = sum(matrix[i])
    toprint = 'Marginal Distribution of Y:\nY - p(Y=i)\n'
    for i, elem in enumerate(margY):
        toprint += f'{i} - {round(elem, 3)}\n'
    print(toprint)
    return margY


def H_X(matrix):
    margX = marginal_X(matrix)
    H = 0
    toprint = 'H(X) ='
    for i in margX:
        if i != 0:
            H += -i * math.log(i, 2)
        toprint += f' -{round(i, 3)}log({round(i, 3)})'
    print(toprint + f' = {round(H, 3)} bits'+'\n')
    return H


def H_Y(matrix):
    margY = marginal_Y(matrix)
    H = 0
    toprint = 'H(Y) ='
    for i in margY:
        if i != 0:
            H += -i * math.log(i, 2)
        toprint += f' -{round(i, 3)}log({round(i, 3)})'
    print(toprint + f' = {round(H, 3)} bits'+'\n')
    return H


def H_XgivenY(matrix):
    margY = marginal_Y(matrix)
    H = 0
    toprint = 'H(X|Y) ='
    for i, p_y in enumerate(margY):
        for j in range(len(matrix[i])):
            p_xgiveny = matrix[i][j] / p_y
            if p_xgiveny != 0:
                H += -p_y * p_xgiveny * math.log(p_xgiveny, 2)
            toprint += f' -{round(p_y, 3)}*{round(p_xgiveny, 3)}log({round(p_xgiveny, 3)})'
    print(toprint + f' = {round(H, 3)} bits'+'\n')
    return H


def H_YgivenX(matrix):
    margX = marginal_X(matrix)
    H = 0
    toprint = 'H(Y|X) ='
    for i in range(len(matrix)):
        for j, p_x in enumerate(margX):
            p_ygivenx = matrix[i][j] / p_x
            if p_ygivenx != 0:
                H += -p_x * p_ygivenx * math.log(p_ygivenx, 2)
            toprint += f' -{round(p_x, 3)}*{round(p_ygivenx, 3)}log({round(p_ygivenx, 3)})'
    print(toprint + f' = {round(H, 3)} bits'+'\n')
    return H


def H_XY(matrix):
    H = 0
    toprint = 'H(X,Y) = '
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                H += - matrix[i][j] * math.log(matrix[i][j], 2)
            toprint += f'-{round(matrix[i][j], 3)}log({round(matrix[i][j], 3)})'
    print(toprint + f' = {round(H, 3)} bits'+'\n')
    return H


def chain_rule1(H_X, H_YgivenX):
    print('Using chain rule formula H(X,Y) = H(X) + H(Y|X):')
    print(f'H(X,Y) = {round(H_X, 3)} + {round(H_YgivenX, 3)} = {round(H_X + H_YgivenX, 3)}'+'\n')
    return H_X + H_YgivenX


def chain_rule2(H_Y, H_XgivenY):
    print('Using chain rule formula H(X,Y) = H(Y) + H(X|Y):')
    print(f'H(X,Y) = {round(H_Y, 3)} + {round(H_XgivenY, 3)} = {round(H_Y + H_XgivenY, 3)}'+'\n')
    return H_Y + H_XgivenY


# Example 3x3
print(f'Calculating entropy for {example3x3}')
probs = convert_to_prob(matrix=example3x3)
h_X = H_X(probs)
h_Y = H_Y(probs)
h_XgivenY = H_XgivenY(probs)
h_YgivenX = H_YgivenX(probs)
h_XY = H_XY(probs)
chain_rule1(h_X, h_YgivenX)
chain_rule2(h_Y, h_XgivenY)

# Example 4x4
print(f'Calculating entropy for {example4x4}')
probs = convert_to_prob(matrix=example4x4)
h_X = H_X(probs)
h_Y = H_Y(probs)
h_XgivenY = H_XgivenY(probs)
h_YgivenX = H_YgivenX(probs)
h_XY = H_XY(probs)
chain_rule1(h_X, h_YgivenX)
chain_rule2(h_Y, h_XgivenY)

# Example 5x5
print(f'Calculating entropy for {example5x5}')
probs = convert_to_prob(matrix=example5x5)
h_X = H_X(probs)
h_Y = H_Y(probs)
h_XgivenY = H_XgivenY(probs)
h_YgivenX = H_YgivenX(probs)
h_XY = H_XY(probs)
chain_rule1(h_X, h_YgivenX)
chain_rule2(h_Y, h_XgivenY)
