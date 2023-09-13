def matrix_addition(a, b):
    linhas = len(a)
    colunas = len(a[0])
    
    nova_matriz = []
    
    for i in range(linhas):
        nova_linha = []
        for j in range(colunas):
            nova_linha.append(a[i][j] + b[i][j])
        nova_matriz.append(nova_linha)
        
    return nova_matriz


print(matrix_addition([[1, 2], [1, 2]], [[2, 3], [2, 3]]))