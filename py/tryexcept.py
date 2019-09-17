try:	# выполнение инструкции, которая может породить исключение
	a = 100/0
except ZeroDivisionError:	# перехват и обработка исключения
	print ('A error')

try:
	b = 2 + '1'
except TypeError:
	print ('B error')

try:
	c = int('qwerty')
except ValueError:
	print ('C error')

d = input("Type something: \n")
try:
	e = 100/int(d)
except ZeroDivisionError:
	print ("Can't divide by zero!")
except ValueError:
	print ("Can't divide without numbers!")
else:	# инструкция выполнится, если исключения не было
	print ("Result = ", e)
finally:	# инструкця выполнится в любом случае
	print ("Thanks, bye!")