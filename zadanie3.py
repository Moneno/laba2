import numpy
import timeit
import copy
import math


def printMatrix(A):
    for strA in A:
        print(strA)


def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def det(A):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0

    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant


def inverse(A):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            tmp = minor(A, i, j)
            if i + j % 2 == 1:
                result[i][j] = -1 * det(tmp) / det(A)
            else:
                result[i][j] = 1 * det(tmp) / det(A)
    return result


def transpose(array):
    res = []
    n = len(array)
    m = len(array[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp+[array[i][j]]
        res = res+[tmp]
    return res


matrix = 0
stroka, stolbec = 3, 3
arr = []
for i in range(stroka):
    temp = []
    for j in range(stolbec):
        temp.append(
            int(input(f'Введите значение элемента {i+1} строки {j+1} столбца\n')))
    arr.append(temp)
matrix = numpy.array(arr)

transMatrix = transpose(matrix)

print('\n')
print(printMatrix(inverse(transMatrix)))
print('\n')
print(numpy.linalg.inv(matrix))

start_time = timeit.default_timer()
inverse(transMatrix)
time1 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
numpy.linalg.inv(matrix)
time2 = timeit.default_timer() - start_time


print(f"\nВремя работы функции {time1}")
print(f"Время работы функции из Numpy {time2}")
