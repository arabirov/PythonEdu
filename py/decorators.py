def my_decorator(function_to_decorate):
    """Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    получая возможность исполнять произвольный код до и после неё. """
    def wrapper_around_the_original_function():
        print("Код, который отработает до вызова функции")
        function_to_decorate()
        print("Функция, которая отработает после вызова функции")
    return wrapper_around_the_original_function()


def standalone_function():
    print('Одинокая функция')


standalone_function = my_decorator(standalone_function)

# ПЕРЕДАЧА ДЕКОРАТОРОМ АРГУМЕНТОВ В ФУНКЦИЮ
@my_decorator  # вызов декоратора используя синтаксис декораторов
def another_standalone():
    print("Leave me alone")


def bread(func):
    def wrapper():
        print()
        func()
        print("<___>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomato")
        func()
        print("~salad~")
    return wrapper


def sandwich(meat="meat"):
    print(meat)


sandwich = bread(ingredients(sandwich))
sandwich()


@bread
@ingredients  # важен порядок декораторов!!!
def sandwich(meat="meat"):
    print(meat)


sandwich()


def decorator_with_args(function_to_decorate):
    def wrapper_with_args(arg1, arg2):
        """передача аргументов декорируемой функции"""
        print("Look what i get: ", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return wrapper_with_args


@decorator_with_args
def print_name(first_name, last_name):
    print("My name is ", first_name, last_name)


print_name("Sasha", "Rabirov")


# ДЕКОРИРОВАНИЕ МЕТОДОВ
def method_decorator(method_to_decorate):
    def method_wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)
    return method_wrapper


class Lucy:
    def __init__(self):
        self.age = 32

    @method_decorator
    def your_age(self, lie):
        print(f"I'm {self.age + lie}, but why do you ask?")


lucy = Lucy()
lucy.your_age(-5)


def function_decorator_arbitrary(function_to_decorate):
    def function_wrapper_arbitrary(*args, **kwargs):
        print("Do you have some?")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
    return function_wrapper_arbitrary


@function_decorator_arbitrary
def function_without_arguments():
    print("No arguments")


function_without_arguments()


@function_decorator_arbitrary
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


@function_decorator_arbitrary
def function_with_named_arguments(a, b, c, platypus="Определенно!"):
    print(f"Любят {a}, {b} и {c} ли утконосов? {platypus}")


function_with_named_arguments("Alex", "Sasha", "Steve", platypus="Естественно!")


# ДЕКОРАТОРЫ С АРГУМЕНТАМИ
def decorator_maker():
    print("I create decorators. I will be called only once: when you ask me to create a decorator.\n")

    def my_decorator_arg(func_arg):
        print("I'm a decorator. I will be called once: in the moment of decorating.\n")

        def wrapped_arg():
            print("I'm a wrapper of function. I will be called every time you call decorating function. "
                  "I return results of decoration function work.\n")
            return func_arg()
        print("I'm returning wrapped function.\n")
        return wrapped_arg
    print("I'm returning decorator.\n")
    return my_decorator_arg


@decorator_maker()
def decorated_function():
    print("I'm decorated function.\n")


# new_decorator = decorator_maker()
# decorated_function = new_decorator(decorated_function)
# decorated_function()
