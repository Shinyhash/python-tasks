matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]

def positive_elements(matrix):
    result = []
    for row in matrix:
        for element in row:
            if element > 0:
                result.append(element)
    return result

result = positive_elements(matrix)
print(result)