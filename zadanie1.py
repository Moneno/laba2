def f(a,c):
    at = []
    for i in range(int(c ** 0.5)):
        if c == 9:
            at.append([a[i],a[i+3],a[i+6]])
        else:
            at.append([a[i],a[i + 2]])
    return at
print('меню')
print('1-транспонировать,2-ранг матрицы ,3-умножение матриц')
k = input()
c = 0
if k == '1':
    print('введите размеры матрицы')
    s = input()
    c = 0
    if s == '1*2':
        a1 = input('введите 1 элемент матрицы ')
        a2 = input('введите 2 элемент матрицы ')
        print(a1)
        print(a2)
    if s == '2*1':
        a1 = input('введите 1 элемент матрицы ')
        a2 = input('введите 2 элемент матрицы ')
        print(a1, ' ', a2)
    if s == '1*3':
        a1 = input('введите 1 элемент матрицы ')
        a2 = input('введите 2 элемент матрицы ')
        a3 = input('введите 3 элемент матрицы ')
        print(a1)
        print(a2)
        print(a3)
    if s == '3*1':
        a1 = input('введите 1 элемент матрицы ')
        a2 = input('введите 2 элемент матрицы ')
        a3 = input('введите 3 элемент матрицы ')
        print(a1, ' ', a2, ' ', a3)
    else:
        a2, a2t = [], []
        if s == '3*3': c = 9
        if s == '2*2': c = 4
        for i in range(c):
            print('введите ', (i + 1), ' элемент матрицы')
            a2.append(int(input()))
        print(f(a2, c))
if k == '2':
    s = input('введите размер матрицы ')
    if s == '3*3':
        n = 9
    else:
        n = 4
    a = []
    for i in range(n):
        print('введите ', (i + 1), ' элемент матрицы')
        a.append(int(input()))
    if n == 4:
        k = -a[2] / a[0]
        a[2] = 0
        a[3] += a[1] * k
        if a[0] * a[3] - a[1] * a[2] != 0:
            print('rang 2')
        else:
            print('rang 1')
    if n == 9:
        k = -a[3] / a[0]
        a[3] = 0
        a[4] += a[1] * k
        a[5] += a[2] * k
        k1 = -a[6] / a[0]
        a[6] = 0
        a[7] += a[1] * k1
        a[8] += a[2] * k1
        k2 = - a[7] / a[4]
        a[7] = 0
        a[8] += a[5] * k2
        if [a[3], a[4], a[5]] == [0, 0, 0] and [a[6], a[7], a[8]] == [0, 0, 0]:
            print('rang 1')
        if [a[3], a[4], a[5]] == [0, 0, 0] or [a[6], a[7], a[8]] == [0, 0, 0]:
            print('rang 2')
        else:
            print('rang 3')
if k == '3':
    print('введите размеры матриц')
    while True:
        s1 = input('введите размер 1й матрицы ')
        s2 = input('введите размер 2й матрицы ')
        if s1 != s2[::-1]:
            print('эти матрицы нельзя перемножить')
        else:
            break
    if s1 in ['2*1', '1*2']:
        n = 2
    if s1 in ['3*1', '1*3']:
        n = 3
    if s1 in ['2*2', '2*2']:
        n = 4
    if s1 in ['3*3', '3*3']:
        n = 9
    a1, a2 = [], []
    for i in range(n):
        print('введите ', (i + 1), ' элемент 1 матрицы')
        a1.append(int(input()))
    for i in range(n):
        print('введите ', (i + 1), ' элемент 2 матрицы')
        a2.append(int(input()))
    c = []
    if len(a1) == 2 and s1 == '2*1':
        c = [[a1[0] * a2[0], a1[0] * a2[1]], [a1[1] * a2[0], a1[1] * a2[1]]]
        print(c)
    if len(a1) == 2 and s1 == '1*2':
        c = [a1[0] * a2[0] + a1[1] * a2[1]]
        print(c)
    if len(a1) == 3 and s1 == '3*1':
        c = [[a1[0] * a2[0], a1[0] * a2[1], a1[0] * a2[2]], [a1[1] * a2[0], a1[1] * a2[1], a1[1] * a2[2]],
             [a1[2] * a2[0], a1[2] * a2[1], a1[2] * a2[2]]]
        print(c)
    if len(a1) == 3 and s1 == '1*3':
        c = [a1[0] * a2[0] + a1[1] * a2[1] + a1[2] * a2[2]]
        print(c)
    if len(a1) == 4:
        c = [[a1[0] * a2[0] + a1[1] * a2[2], a1[0] * a2[1] + a1[1] * a2[3]],
             [a1[2] * a2[0] + a1[3] * a2[2], a1[2] * a2[1] + a1[3] * a2[3]]]
        print('произведение равно', c)
    a2t = []
    if len(a1) == 9:
        for i in range(3):
            a2t.append(a2[i])
            a2t.append(a2[i + 3])
            a2t.append(a2[i + 6])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                c.append(a1[i] * a2t[j] + a1[i + 1] * a2t[j + 1] + a1[i + 2] * a2t[j + 2])
        print('произведние равно', c)