a = set()
print(a)
a = set('hello')
print(a)
a = {'a', 'b', 'c', 'd'}  # множества имеют тот же литерал, что и словари, но множество нельзя создать пустым!
print(a)
a = {i ** 2 for i in range(100)}
print(a)
words = ['hi', 'mom', 'word', 'hi']
print(set(words))  # при помощи множеств можно избавлятся от повторяющихся элементов
if 'hi' in set(words):
    print('yes')
a.copy()  # копирует множество
print(a)
a.discard(0)  # удаляет элемент из множества
print(a)
print(len(a))  # длина множества
b = set()
b = {1, 2, 3, 81, 25, 36, 39, 13}
print(b)
print(set.intersection(a, b))  # пересечение множеств
c = set()
c = set.union(a, b)  # объединение множеств
c.add('-----93-----')  # добавляет элемент в множество
print(c)

d = frozenset('qwerty')  # frozenset - неизменяемое множество
e = set('qwerty')
print(e == d)
