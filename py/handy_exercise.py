import sys
import os
import exercise

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# first_arg_input = int(input("Input first argument: \n"))
# second_arg_input = int(input("Input second argument: \n"))
# operation_input = input("Input operation: \n")
# exercise.arithmetic(first_arg_input, second_arg_input, operation_input)
#
# year_input = int(input("Input year for check: \n"))
# exercise.is_year_leap(year_input)
#
# side_input = int(input("Input side size: \n"))
# print(exercise.square(side_input))
#
# month_input = int(input("Input month number: \n"))
# exercise.season(month_input)
#
# years_input = int(input("Input amount of years: \n"))
# a_input = int(input("Input amount of money: \n"))
# exercise.bank(a_input, years_input)

# is_prime_arg_input = input("Input digit from 0 to 1000: \n")
# if is_prime_arg_input.isdigit() and 0 <= int(is_prime_arg_input) <= 1000:
#     exercise.is_prime(int(is_prime_arg_input))
#
# day_input = int(input("Input day: \n"))
# month_input = int(input("Input month: \n"))
# year_input = int(input("Input year: \n"))
# exercise.date_exists(day_input, month_input, year_input)

string_input = input("Input string: \n")
key_input = int(input("Input key: \n"))
encr_str = exercise.xor_cipher(string_input, key_input)
print("Encrypted string: \n", encr_str)
print("Decrypted string: \n", exercise.xor_cipher(encr_str, key_input))
