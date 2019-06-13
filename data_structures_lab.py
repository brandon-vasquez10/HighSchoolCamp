"""

title: data_structures_lab
author: Brandon
date: 2019-06-13 11:32
"""

import random


def shake_ball():
    options = ["Yes definitely", "As I see it, yes", "Ask again later", "Cannot predict now", "Don't count on it")]
    input("Enter a question: ")
    rnd_num = random.randint(0, len(options) - 1)
    return options[rnd_num]

print(shake_ball())