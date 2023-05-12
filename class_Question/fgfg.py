def spiral_matrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    num = 1
    for layer in range((n + 1) // 2):
        for i in range(layer, n - layer):
            matrix[layer][i] = num
            num += 1
        for i in range(layer + 1, n - layer):
            matrix[i][n - layer - 1] = num
            num += 1
        for i in range(layer + 1, n - layer):
            matrix[n - layer - 1][n - i - 1] = num
            num += 1
        for i in range(layer + 1, n - 1 - layer):
            matrix[n - i - 1][layer] = num
            num += 1
    return matrix

print(spiral_matrix(3))
