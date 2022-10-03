def f(a,c):
    at = []
    for i in range(int(c ** 0.5)):
        if c == 9:
            at.append(a[i])
            at.append(a[i + 3])
            at.append(a[i + 6])
        else:
            at.append(a[i])
            at.append(a[i + 2])
    return at
print('меню')
print('1-транспонировать')
k = input()
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
    print(a1,' ',a2)
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
    print(a1, ' ', a2,' ',a3)
else:
    a2,a2t = [],[]
    if s == '3*3': c = 9
    if s == '2*2': c = 4
    for i in range(c):
        print('введите ', (i + 1), ' элемент матрицы')
        a2.append(int(input()))
    print(f(a2,c))

