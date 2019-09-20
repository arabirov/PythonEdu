class A:  # создание класса
    pass


a = A()  # создание экземпляра класса
b = A()

a.arg = 1  # добавление атрибута arg экземпляру a
b.arg = 2

print(a.arg, b.arg)


class B:
    def g(self):
        """self - обязательный аргумент
        содержащий в себе экземпляр класса,
        передающийся при вызове метода.
        """
        return 'Hello world!'


c = B()
print(c.g())


class C:
    def fibonacci(self, position):
        fibo = []
        start = 0
        start1 = 1
        index = 0
        while index < position:
            fibo[index:index + 1] = [start]
            start, start1 = start1, start + start1
            index += 1
            if index >= position:
                return fibo


your_number = input("Enter number: \n")
new_fibo = C()
if your_number.isdigit() and int(your_number) > 0:
    print("Sequence: ", new_fibo.fibonacci(int(your_number)), "\n")
else:
    print("Please, use only positive digits")

