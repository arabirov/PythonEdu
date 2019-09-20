import time
import random

list('слово')
s = []
la = ['s', 'p', ['isok']]  # создание списка
li = [1, 2912, 213.1, 0, -1, 2]
print('{1}'.format(*la))  # * нужна для работы со списками без явного указания на format
print('{0[1]}'.format(la))  # вариант без *

c = [z * 2 for z in la]  # генерация списка, в конце может использоваться list(l)
print(c, '\n-----------------------------------------------')

c1 = [x * 2 for x in list(la) if x != ['isok']]  # более сложная генерация списка
print(c1, '\n-----------------------------------------------')

c2 = [list(j) + list(d) for j in list(la) if j != 'p' for d in list('word') if
      d != 'd']  # еще более сложная генерация списка
print(c2, '\n-----------------------------------------------')

li.sort()
print(li, '\n-----------------------------------------------')
# сортировка списка. В отличие от строк, значения не надо передавать в переменную, т.к. изменяется весь список

a = [66.25, 333, 333, 1, 1234.5, 22, 20, -5, 23]
print('count = ', a.count(333), a.count(1), a.count('q'))  # подсчёт количества выбранных элементов в списке
a.insert(3, -1)  # вставить на выбранную позицию (3) элемент (-1)
a.append(12345)  # вставить элемент в конец списка
print('insert and append = ', a)
print('index = ', a.index(-5))  # вывод индекса выбранного элемента
a.remove(20)  # удаление выбранного элемента
print('remove = ', a)
a.reverse()  # реверс списка
print('reverse = ', a)
a.sort()  # сортировка списка
print('sort = ', a, '\n-----------------------------------------------')

print('index[0] = ', a[0])
print('index[-1] = ', a[-1])
print(len(a))  # вывод длины списка

i = 0
b = []
print('Starting...')
while i < len(a):
    print(f'index[{i}] =  {a[i]}')  # вывод значений по индексам
    n = random.randrange(3.0)
    time.sleep(n)
    b[i:i + 1] = [n]
    print(f'Time[{i}] = {b[i]} second(s)')
    i += 1
    if i >= len(a):
        print(f'Full index = {a}\n', f'Full time = {b}\n', 'Time summary = ', sum(b), 'seconds')
        print('End', '\n-----------------------------------------------')

print(a[3:6:1])  # срез списка (Start:Stop:Step)
a[3:6] = [0, 0, 0, 0]  # добавление/замена элементов с 3 по 6
del a[1:2]  # удаление элементов с 1 по 2
print('changed and cutted = ', a)
print(len(a))
print(a.__sizeof__())

p = 0
e = []
y = []
while p < 15:
    r = random.randrange(-1000, 1000)
    tr = random.randrange(3.0)
    e[p:p + 1] = [r]
    y[p:p + 1] = [tr]
    print(f'index[{p}] =  {e[p]}')  # вывод значений по индексам
    time.sleep(tr)
    print(f'Time[{p}] = {y[p]} second(s)')
    p += 1
    if p >= 15:
        print(f'Full index = {e}')
        e.sort()
        print(f'Sorted index = {e}\n' f'Full time = {y}\n', 'Time summary = ', sum(y), 'seconds')
        print('End', '\n{-----------------------------------------------')
