import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("Invalid operating system. Please use Windows, Mac, or Linux")


def is_response_yes(i):
    return i in ["y", "yes"]

def is_response_yes_or_enter(i):
    return i in ["y", "yes"] or i == ""

def is_response_no(i):
    return i in ["n", "no"]