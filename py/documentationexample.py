def new_func(n):
    """передаётся ссылка на myfunc, 100 берётся из области видимости new_func
    передаётся 200 в my_func, результат 300, т.к. 200 находится в области видимости my_func, а 100 в области видимости выше
    """
    def my_func(l):
        return n + l

    return my_func


new = new_func(100)
print(new(200))

print(new_func.__doc__)
