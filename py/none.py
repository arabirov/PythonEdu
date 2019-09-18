none_variable = None
print(type(none_variable))
try:
    a = 1/none_variable
except TypeError:
    print("Oopsie")
finally:
    print("What did you expect?")
if none_variable == None:
    print("None")
if none_variable is None:
    print("None 2")


class MyClass:
    def __eq__(self, my_object):
        return True


my_class = MyClass()
if my_class == None:
    print("None")
if my_class is None:  # проверка на None должна быть ТОЛЬКО с испльзованием is
    print("None 2")
