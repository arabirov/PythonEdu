S1 = 'spam'  # создание строковой переменной
S2 = 'kek'
print((S1[0] + 'b' + S2[1:]).title())  # принт с заглавной
print((S1[0] + 'b' + S2[1:]).zfill(20))  # принт с заполнением до 20 символов
print((S1[0] + 'b' + S2[1:]).upper())  # принт всего апперкейсом
print(('{0} {1} {0}').format(S1, S2))

S3 = {'not lul': 'lol', 'not lol': 'lul'}  # создание именованной строки
print(('Lul and lol: {not lul}, {not lol}').format(**S3))  # вывод именованной строки
print(('Your number is : {S4[1]!r}').format(S4=['1', '2', '3']))  # вывод символов во "внутреннем представлении"
print(('{:>30}; {:<30}').format(3.14, -3.14))  # вывод с отступом

points = 67
total = 200
print(('Result: {:.0%}').format(points / total))  # вывод результата в процентах

name = 'Alex'
age = 24
print("1 Hi! My name is " + name + ", I'm " + str(age) + " years old.")  # один из вариантов передачи переменной в print
print("2 Hi! My name is %s, I'm %d years old." % (name, age))  # один из вариантов передачи переменной в print
print("3 Hi! My name is %(name)s, I'm %(age)d years old." % {"name": name,
                                                             "age": age})  # один из вариантов передачи переменной в print
print("4 Hi! My name is {}, I'm {} years old.".format(name, age))  # один из вариантов передачи переменной в print
print("5 Hi! My name is {name}, I'm {age} years old.".format(age=age,
                                                             name=name))  # один из вариантов передачи переменной в print
print(f"6 Hi! My name is {name}, I'm {age} years old.")  # один из вариантов передачи переменной в print
