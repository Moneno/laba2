import numpy as np

operation = input(
    'Введите название операции: (транспонирование, умножение, определение ранга)\n').lower()


def createMatrix(sizes):
    size = input(f'Введите размер матрицы: ({sizes})\n')
    stroka, stolbec = int(size[0]), int(size[2])
    arr = []
    for i in range(stroka):
        temp = []
        for j in range(stolbec):
            temp.append(
                int(input(f'Введите значение элемента {i+1} строки {j+1} столбца\n')))
        arr.append(temp)
    matrix = np.array(arr)
    return matrix


def transpon():
    matrix = createMatrix('1x2, 2x1, 1x3, 3x1, 2x2, 3x3')
    matrix = np.transpose(matrix)
    print(f'Ответ:\n{matrix}')


def product():
    matrix1 = createMatrix('1x2, 2x1, 1x3, 3x1, 2x2, 3x3')
    print(matrix1)
    matrix2 = createMatrix('1x2, 2x1, 1x3, 3x1, 2x2, 3x3')
    print(matrix2)
    matrixprod = np.dot(matrix1, matrix2)
    print(f'Ответ:\n{matrixprod}')


def rang():
    matrix = createMatrix('2x2, 3x3')
    matrixRang = np.linalg.matrix_rank(matrix)
    print(f'Ответ:\n{matrixRang}')


if (operation == 'транспонирование'):
    transpon()
elif (operation == 'умножение'):
    product()
elif (operation == 'определение ранга'):
    rang()
