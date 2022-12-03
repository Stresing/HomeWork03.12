def task1():
    #Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
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


task = int(input("Какую задачу желаете проверить? "))
if task == 1:
    task1()

elif task ==2:
    task2()
elif task == 3:
    task3()