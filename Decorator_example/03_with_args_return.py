
# def decorate_it_with_args_return(func):
#     def adding_extra_behaviour(*args, **kwargs):
#         print("**"*10)
#         result = func(*args, **kwargs)
#         print("**"*10)
#         return result

#     return adding_extra_behaviour

from decorators import decorate_it_with_args_return

@decorate_it_with_args_return
def print_name(name):
    print(f"Hi from {name}")
    return "welcome to my YouTube channel"

result = print_name("Sunny")
print(result)