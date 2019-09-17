your_number = input("Enter number: \n")


def fibonacci(a):
    b = []
    c = 0
    d = 1
    i = 0
    while i < a:
        b[i:i + 1] = [c]
        c, d = d, c + d
        i += 1
        if i >= a:
            return b


if your_number.isdigit() and int(your_number) > 0:
    print("Sequence: ", fibonacci(int(your_number)), "\n")
else:
    print("Please, use only positive digits")
