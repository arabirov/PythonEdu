int1 = int(input("Input first digit\n"))  # ввод символов с клавиатуры
int2 = int(input("Input second digit\n"))

if (0 <= int1 + int2 < 10):  # начало условия
    print("True")
elif (int1 + int2 < 0):  # подусловие
    print("kek")
else:  # конец условия
    print("False")


def func(int1, int2):  # создание функции
    return int(int1 + int2)  # возврат результата функции


A = "lol" if func(int1, int2) < 100 else "lul"  # вариант условия в 1 строку
print(A + " second check")

o = func(int1, int2)
while o < 20:  # цикл while
    print('kek', 'o = ', o)
    o = o + 1

for i in A:  # цикл for
    if i == "u":
        break
else:
    print("not lul")

K = b'\x00\x10'  # битовая переменная
T = int(1.1)  # представление float в целочисленном виде
print(T.to_bytes(5, byteorder="big"), "\n",
      int.from_bytes(b'\x00\x10', byteorder="big"))  # вывод int в byte и byte в int
