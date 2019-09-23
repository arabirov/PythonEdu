class MyClass:
    def __init__(self, a, b):  # инициализация экземпляра класса
        self.a = a
        self.b = b

    def __len__(self):  # объявление класса для вычисления длины объекта
        return len(self.a), len(str(self.b))

    def __add__(self, c, d):  # объявление класса со своими переменными
        return c + d

    def __mul__(self, e, f):  # возврат print()
        return print(e + f)


A = MyClass('Sasha', 24)
print(f"Hi! My Name is {A.a}, I'm {A.b} years old.")
print(A.__len__())
print(f"Add = {A.__add__(1, 2)}")
A.__mul__(5, 10)
