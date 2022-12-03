def task1():
    # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    checkNumb = int(input("Введите цифру, для проверки на день недели: "))

    if 6 <= checkNumb <= 7:
        print(f"День: {checkNumb} - выходной")
    elif 0 < checkNumb < 6:
        print(f"День: {checkNumb} - рабочий")
    else:
        print("Число за пределами страндартных 7ми дней")


def task2():
    # Напишите программу для. Проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

    # not (X or Y or Z) = not X and not Y and not Z
    print('x,y,z')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, 'AND', y, 'OR', z, '=', x and y or z)


def task3():
    # Напишите программу, которая принимает на вход координаты точки (X и Y),
    # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
    # в которой находится эта точка (или на какой оси она находится)

    x = int(input("Введите точку X: "))
    y = int(input("Введите точку Y: "))

    chek = x != 0
    chek2 = y != 0
    if chek and chek2:
        if x > 0 and y > 0:
            print("Точка принадлежит Первой четверти координат")
        elif x < 0 and y > 0:
            print("Точка принадлежит Второй четвети координат")
        elif x < 0 and y < 0:
            print("Точка принадлежит Третьей четвети координат")
        elif x > 0 and y < 0:
            print("Точка принадлежит Четвертой четверти координат")
    else:
        print("По условию задачи точки не равны 0, попробуйте снова")


def task4():
    # Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
    num_chetvert = int(input("Введите номер интересующей вас четверти: "))
    if num_chetvert == 1:
        print(f"Диапазон возможных координат Y и X в четверти № {num_chetvert}  от 0 до +∞ ")
    elif num_chetvert == 2:
        print(f"Диапазон возможных координат Y(0 до +∞)  X(0 до -∞) в {num_chetvert} четверти.")
    elif num_chetvert == 3:
        print(f"Диапазон возможных координат Y и X в четверти № {num_chetvert}  от 0 до -∞ ")
    elif num_chetvert == 4:
        print(f"Диапазон возможных координат Y(0 до -∞)  X(0 до +∞) в {num_chetvert} четверти.")
    else:
        print("Всего четвертей 4, попробуйте снова")


def task5():
    #Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

    import math

    x_coordinat_one = int(input("Введите Х координат первой точки: "))
    y_coordinat_one = int(input("Введите Y координат первой точки: "))
    x_coordinat_two = int(input("Введите Х координат второй точки: "))
    y_coordinat_two = int(input("Введите Y координат второй точки: "))
    sum = math.sqrt((x_coordinat_two - x_coordinat_one) ** 2 + (y_coordinat_two - y_coordinat_one) ** 2)
    print(round(sum, 2))


task = int(input("Какую задачу желаете проверить? "))
if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()
elif task == 4:
    task4()
elif task == 5:
    task5()
