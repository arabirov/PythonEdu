a = ((1, 2, 3, 4, 5),1)	# кортеж
b = tuple((1, 2, 3, 4, 5))	# кортеж
c = {(1, 2, 3, 4, 5) : 1}	# кортеж как часть словаря
d = 1,	# кортеж без ()
e = tuple('hello world!')	# кортеж из итерируемого объекта
a, b = b, a
print (a)
print (b)
print (c)
print (d)
print (e)