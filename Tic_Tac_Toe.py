# Инициализация пустого поля 3х3
table = [['-'] * 3, ['-'] * 3, ['-'] * 3]

#    - -> пустое поле
#    0 -> нолик
#    1 -> крестик

# Счетчик (в цикле - если делится на 2, то крестик ходит)
count = 2

while True:

    # Вывод поля
    for i in table:
        for j in i:
            print(j, end=' ')
        print()

    # -----------------Проверки-----------------

    # Горизонтальные нули
    if ((table[0][0] == table[0][1] == table[0][2] == 0)
            or (table[1][0] == table[1][1] == table[1][2] == 0)
            or (table[2][0] == table[2][1] == table[2][2] == 0)
            # Вертикальные нули
            or (table[0][0] == table[1][0] == table[2][0] == 0)
            or (table[0][1] == table[1][1] == table[2][1] == 0)
            or (table[0][2] == table[1][2] == table[2][2] == 0)
            # Диагональные нули
            or (table[0][0] == table[1][1] == table[2][2] == 0)
            or (table[0][2] == table[1][1] == table[2][0] == 0)):
        print('Нолики победили')
        break

    # Горизонтальные крестики
    if ((table[0][0] == table[0][1] == table[0][2] == 1)
            or (table[1][0] == table[1][1] == table[1][2] == 1)
            or (table[2][0] == table[2][1] == table[2][2] == 1)
            # Вертикальные крестики
            or (table[0][0] == table[1][0] == table[2][0] == 1)
            or (table[0][1] == table[1][1] == table[2][1] == 1)
            or (table[0][2] == table[1][2] == table[2][2] == 1)
            # Диагональные крестики
            or (table[0][0] == table[1][1] == table[2][2] == 1)
            or (table[0][2] == table[1][1] == table[2][0] == 1)):
        print('Крестики победили')
        break

    # -----------------Конец проверок-----------------

    # Ввод двух координат через пробел
    coord = input().split()

    # Проверка на некорректный ввод
    while True:
        # Проверка наличия двух элементов в списке "coord"
        if ((len(coord) == 2)
                # Проверка символов на то, что это числа
                and (coord[0].isnumeric() and coord[1].isnumeric())
                # Проверка длины каждого элемента списка "coord"
                and ((len(coord[0]) and len(coord[1])) == 1)
                # Проверка корректного значения (индекс должен быть в пределах от 0 до 2 включительно)
                and ((int(coord[0]) and int(coord[1])) >= 0)
                and ((int(coord[0]) and int(coord[1])) <= 2)):
            break
        else:
            coord = input('Try again: ').split()

    # Проверка, кто сейчас ходит: крестик или нолик
    if count % 2 == 0:
        table[int(coord[0])][int(coord[1])] = 1
    else:
        table[int(coord[0])][int(coord[1])] = 0

    count += 1
