#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number / 10

if number >= 0:
    last = number % 10
else:
    last = (-number % 10) * -1

msg = F"Last digit of {number} is {last}"

if last == 0:
    print(F"{msg} and is 0")
elif last > 5 and last % 10 != 0:
    print(F"{msg} and is greater than 5")
else:
    print(F"{msg} and is less than 6 and not 0")
