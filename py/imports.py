import math as m  # использование псевдонима
import time
import os
import my_fibonacci  # импорт собственного модуля

from pathlib import Path  # импорт конкретного атрибута
from sys import *  # импорт конкретного атрибута

print(m.pi)
print(os.getcwd())

your_number = input("Enter number: \n")
if your_number.isdigit() and int(your_number) > 0:
    print("Sequence: ", my_fibonacci.fibonacci(int(your_number)), "\n")
else:
    print("Please, use only positive digits")
