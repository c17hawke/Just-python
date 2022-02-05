
# def decorate_it_with_args(func):
#     def adding_extra_behaviour(*args, **kwargs):
#         print("**"*10)
#         func(*args, **kwargs)
#         print("**"*10)

#     return adding_extra_behaviour

from decorators import decorate_it_with_args

@decorate_it_with_args
def print_name(name):
    print(f"Hi from {name}")

print_name("Sunny")
print_name("c17hawke")
