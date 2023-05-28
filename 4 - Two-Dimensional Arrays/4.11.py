matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]

def positiveE(matrix):
    result = []
    for row in matrix:
        for element in row:
            if element > 0:
                result.append(element)
    return result

result = positiveE(matrix)
print(result)