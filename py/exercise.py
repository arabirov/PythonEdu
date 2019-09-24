
from math import sqrt
from datetime import datetime


# FIRST EXERCISE
def arithmetic(first_arg, second_arg, operation):
    if operation is "-":
        print(first_arg - second_arg)
    elif operation is "+":
        print(first_arg + second_arg)
    elif operation is "*":
        print(first_arg * second_arg)
    elif operation is "/":
        print(first_arg / second_arg)
    else:
        print("Please, use only  + - * / operations")


if __name__ == "__main__":
    first_arg_input = int(input("Input first argument: \n"))
    second_arg_input = int(input("Input second argument: \n"))
    operation_input = input("Input operation: \n")
    arithmetic(first_arg_input, second_arg_input, operation_input)


# SECOND EXERCISE
def is_year_leap(year):
    if year % 4:
        print("Year is not leap!")
    else:
        print("Year is leap!")


if __name__ == "__main__":
    year_input = int(input("Input year for check: \n"))
    is_year_leap(year_input)


# THIRD EXERCISE
def square(side):
    perimeter = side * 4
    area = side ** 2
    diagonal = side * sqrt(2)
    return tuple((perimeter, area, diagonal))


if __name__ == "__main__":
    side_input = int(input("Input side size: \n"))
    print(square(side_input))


# FOURTH EXERCISE
def season(month):
    if 0 < month < 3 or month == 12:
        print("Winter")
    elif 3 <= month < 6:
        print("Spring")
    elif 6 <= month < 9:
        print("Summer")
    elif 9 <= month < 12:
        print("Fall")
    else:
        print("Please, use only digits from 1 to 12")


if __name__ == "__main__":
    month_input = int(input("Input month number: \n"))
    season(month_input)


# FIFTH EXERCISE
def bank(a, years):
    i = 0
    while i < years:
        a = a * 1.1
        i += 1
        if i >= years:
            return print(f"Years = {years}, Money = {a}")


if __name__ == "__main__":
    years_input = int(input("Input amount of years: \n"))
    a_input = int(input("Input amount of money: \n"))
    bank(a_input, years_input)


# SIXTH EXERCISE
def is_prime(is_prime_arg):
    i = 2
    limit = int(sqrt(is_prime_arg))
    while i <= limit:
        if is_prime_arg % i == 0:
            print("False")
            quit()
        i += 1
    print("True")


if __name__ == "__main__":
    is_prime_arg_input = input("Input digit from 0 to 1000: \n")
    if is_prime_arg_input.isdigit() and 0 <= int(is_prime_arg_input) <= 1000:
        is_prime(int(is_prime_arg_input))


# SEVENTH EXERCISE
def date_exists(day, month, year):
    try:
        if datetime.strptime(f"{day}.{month}.{year}", "%d.%m.%Y"):
            print("Date exists!")
    except ValueError:
        print("Date does not exist!")


if __name__ == "__main__":
    day_input = int(input("Input day: \n"))
    month_input = int(input("Input month: \n"))
    year_input = int(input("Input year: \n"))
    date_exists(day_input, month_input, year_input)


# EIGHTH EXERCISE
