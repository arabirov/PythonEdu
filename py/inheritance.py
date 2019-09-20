class MyList(dict):  # создание класса, похожего на словарь, dict - наследование от базового класса
    def get(self, key, default=0):
        """класс ведёт себя так же, как и словарь,
        но возвращает 0 вместо None
        """
        return dict.get(self, key, default)


a = dict(a=1, b=2, c=3)
b = MyList(a=1, b=2, c=3)
b['d'] = 4
print(a, '\n', b, '\n', a.get('v'), '\n', b.get('v'))
