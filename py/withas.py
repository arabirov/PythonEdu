with open('../files/read_file2.txt', 'w') as g:  # оборачивание выполнения блока инструкций менеджером контекста
    d = int(input())
    print(f'1 / {d} = {1/d}', file=g)
