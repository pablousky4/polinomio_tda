def determinante_recursivo(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    det = 0
    for i in range(3):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        det += ((-1) ** i) * matriz[0][i] * determinante_recursivo(submatriz)
    return det

def determinante_iterativo(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def ejecutar_determinantes(matriz):
    det_recursivo = determinante_recursivo(matriz)
    det_iterativo = determinante_iterativo(matriz)

    print(f"Determinante recursivo: {det_recursivo}")
    print(f"Determinante iterativo: {det_iterativo}")
    return det_recursivo, det_iterativo

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ejecutar_determinantes(matriz)