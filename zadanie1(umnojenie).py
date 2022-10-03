print('введите размеры матриц')
while True:
    s1 = input('введите размер 1й матрицы ')
    s2 = input('введите размер 2й матрицы ')
    if s1 != s2[::-1]:
        print('эти матрицы нельзя перемножить')
    else: break
if s1 in ['2*1','1*2']:
    n = 2
if s1 in ['3*1','1*3']:
    n = 3
if s1 in ['2*2','2*2']:
    n = 4
if s1 in ['3*3','3*3']:
    n = 9
a1,a2 = [],[]
for i in range(n):
    print('введите ', (i+1),' элемент 1 матрицы')
    a1.append(int(input()))
for i in range(n):
    print('введите ', (i+1),' элемент 2 матрицы')
    a2.append(int(input()))
c = []
if len(a1) == 2 and s1 == '2*1':
    c = [[a1[0]*a2[0],a1[0]*a2[1]],[a1[1]*a2[0],a1[1]*a2[1]]]
    print(c)
if len(a1) == 2 and s1 == '1*2':
    c = [a1[0]*a2[0] + a1[1]*a2[1]]
    print(c)
if len(a1) == 3 and s1 == '3*1':
    c = [[a1[0]*a2[0],a1[0]*a2[1],a1[0]*a2[2]],[a1[1]*a2[0],a1[1]*a2[1],a1[1]*a2[2]],[a1[2]*a2[0],a1[2]*a2[1],a1[2]*a2[2]]]
    print(c)
if len(a1) == 3 and s1 == '1*3':
    c = [a1[0]*a2[0] + a1[1]*a2[1] + a1[2]*a2[2]]
    print(c)
if len(a1) == 4:
    c = [[a1[0] * a2[0] + a1[1]*a2[2] ,a1[0]*a2[1] + a1[1] * a2[3]],[a1[2]*a2[0] + a1[3]*a2[2] , a1[2]*a2[1]+ a1[3]*a2[3]]]
    print('произведение равно',c)
a2t = []
if len(a1) == 9:
    for i in range(3):
        a2t.append(a2[i])
        a2t.append(a2[i+3])
        a2t.append(a2[i+6])
    for i in range(0,9,3):
        for j in range(0,9,3):
            c.append(a1[i]*a2t[j] + a1[i+1]*a2t[j+1] + a1[i+2]*a2t[j+2])
    print('произведние равно',c)