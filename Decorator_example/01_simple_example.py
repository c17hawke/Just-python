
# def decorate_it(func):
#     def adding_extra_behaviour():
#         print("**"*10)
#         func()
#         print("**"*10)

#     return adding_extra_behaviour

# def print_name():
#     print("Hi from Sunny")

# print_name()

# first way

# my_name = decorate_it(print_name)
# my_name()

# 2nd way
from decorators import decorate_it

@decorate_it
def print_name():
    print("Hi from Sunny")

print_name()

@decorate_it
def print_welcome():
    print("Welcome to my youtube channel")

print_welcome()