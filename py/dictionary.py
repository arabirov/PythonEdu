d = {'dict': 1, 'dict2': 2}  # вариант создания словаря
print(d)
d1 = dict(short='dict', long='dictionary')  # вариант создания словаря при помощи функции dict()
print(d1)
d2 = dict([(1, 2), (3, 4)])  # вариант создания словаря с кортежами
print(d2)
d3 = dict.fromkeys(['a', 'b'])  # вариант создания словаря с использованием метода fromkeys()
print(d3)
d4 = dict.fromkeys(['a', 'b'], 100)  # вариант создания словаря с использованием метода fromkeys()
print(d4)
a = 0
d5 = {a: a + 1 for a in range(7)}  # вариант создания словаря при помщи генерации
print(d5, '\n-----------------------------------------------')
d6 = dict({1: 2, 3: 4, 5: 6})
print(d6[1])
d6[8] = 7  # добавление ключа в словарь, так же ключ можно перезаписать
print(d6)
print(dict.keys(d6))  # вывод ключей словаря
print('Popped value = ', d6.popitem(), '\n', 'Result = ', d6)
print('Non-existing key = ', d6.get(6))  # вывод несуществующего ключа
print('Cleared dictionary = ', d6.clear())  # вывод очищенного словаря
