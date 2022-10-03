print('введите размеры матрицы')
s = input('введите размер матрицы ')
if s == '3*3':
    n = 9
else: n =4
a = []
for i in range(n):
    print('введите ', (i+1),' элемент матрицы')
    a.append(int(input()))
if n == 4:
    k = -a[2]/a[0]
    a[2] = 0
    a[3] += a[1]*k
    if a[0]*a[3] - a[1]*a[2] != 0:
        print('rang 2')
    else: print('rang 1')
if n == 9:
    k = -a[3]/a[0]
    a[3] = 0
    a[4] += a[1]*k
    a[5] += a[2] * k
    k1 = -a[6]/a[0]
    a[6] = 0
    a[7] += a[1]*k1
    a[8] += a[2]*k1
    k2 = - a[7]/a[4]
    a[7] = 0
    a[8] += a[5]*k2
    if [a[3],a[4],a[5]] == [0,0,0] and [a[6],a[7],a[8]] == [0,0,0]:
        print('rang 1')
    if [a[3],a[4],a[5]] == [0,0,0] or [a[6],a[7],a[8]] == [0,0,0]:
        print('rang 2')
    else: print('rang 3')
