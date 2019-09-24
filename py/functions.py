import random

kek = int(input("Input digit\n"))
a = 8
b = 7


def add(x, y):  # создание функции, передача аругметов в неё
    return x + y


print(add(a, b))


def new_func(n):
    def my_func(l):
        return n + l
    return my_func


new = new_func(100)  # передаётся ссылка на myfunc, 100 берётся из области видимости newfunc
print(new(
    200))  # передаётся 200 в myfunc, результат 300, т.к. 200 находится в области видимости myfunc, а 100 в области видимости выше


def func():
    pass  # функция вернёт None


def func1(a, b, c=3):
    return a + b + c


print(func1(a, b))


def func2():
    def func3():
        set1 = set()
        i = 0
        for i in range(15):
            n = random.randrange(100)
            k = (n ** 2)
            # print (k)
            set1.add(k)
            i += 1
            if i >= 15:
                return set1

    return func3()  # передача функции (не ссылки)


print(func2(), '\n-----------------------------------------------')


# ---------------------------ИЛИ-----------------------------
def func4(kek):  # передача значения в функцию
    def func5():
        set1 = set()
        i = 0
        while i < 15:
            n = random.randrange(kek)
            set1.add(n ** 2)
            set(set1)
            i += 1
            if i >= 15:
                return set1

    return func5  # передача ссылки на функцию


new = func4(kek)  # вызов функции
print(new(), '\n-----------------------------------------------')


def func6(*args):  # функция принимает переменное кол-во позиционных аргументов
    return args  # функция возвращает кортеж


print(func6(1, 2, 3, 'abc'))
print(func6(1))


def func7(**kwargs):  # функция принимает переменное кол-во именованных аргументов
    return kwargs  # функция возвращает словарь


print(func7(a1=1, a2=2, a3=3, a4='abc'))
print(func7(a='python'))
