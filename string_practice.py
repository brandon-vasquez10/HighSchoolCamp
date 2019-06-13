"""

title: string_practice
author: Brandon
date: 2019-06-11
"""
# strings_lab

#answer = input("Enter a letter:  ")
#print(answer in "qwertyuiopasdfghjklzxcvbnm")


def is_letter(character):
    return character.lower() in "qwertyuiopasdfghjklzxcvbnm"


print(is_letter("isadfasdf"))
print(is_letter("0"))

def short_hand(short):
    short = short.lower().replace("and", "&").replace("too", "2").replace("you", "u").replace("for", "4")
    short = short.replace("a", "").replace("e", "").replace("i", "").replace("o", "")
    return short
print(short_hand("Thank you for that! You are too sweet and kind"))
print(short_hand("How are you today"))


def removing(check):
    check = check.lower().replace("QWERTYUIOPASDFGHJKLZXCVBNM", "qwertyuiopasdfghjklzxcvbnm")
    check = check.replace(",", " ").replace("'", " ").replace(" ", "")
    return check


print(removing("Madam, I'm Adam"))

def palindrome(check):
    check = removing(check)
    return check == check[::-1]


print(palindrome("Madam, I'm Adam"))
print(palindrome("Computer"))

