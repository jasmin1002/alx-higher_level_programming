#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Your code here
if number < 0:
    print(f"{number:d} is negative")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is positive")
