"""

title: random_practice
author: Brandon
date: 2019-06-12 09:53
"""
#random_salary
import random

name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
print(name, "your current salary is", salary)
raise_per = random.randint(0, 100)
raise_amount = salary * (raise_per/100) + salary
print(f"Your raise is {raise_per}% of {salary}")
print(name, "your new salary is", raise_amount)
