class C:
    arg = "Hi"
    """все экземпляры этого класса будут иметь атрибут arg"""
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
        # return self.arg

    def _private(self):
        """_ делает атрибут(метод) приватным, доступным только внутри методов класса"""
        return "This is private method!"
    def __private(self):
        """__ делает атрибут(метод) недоступным по имени"""
        return "This also is private method!"


your_number = input("Enter number: \n")
new_fibo = C()
if your_number.isdigit() and int(your_number) > 0:
    print("Sequence: ", new_fibo.fibonacci(int(your_number)), "\n")
else:
    print("Please, use only positive digits")
print(new_fibo.arg)
print(new_fibo._private())
print(new_fibo._C__private())  # атрибут с __ остается доступным под именем _ИмяКласса__ИмяАтрибута
