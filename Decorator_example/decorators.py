def decorate_it(func):
    def adding_extra_behaviour():
        print("**"*10)
        func()
        print("**"*10)

    return adding_extra_behaviour


def decorate_it_with_args(func):
    def adding_extra_behaviour(*args, **kwargs):
        print("**"*10)
        func(*args, **kwargs)
        print("**"*10)

    return adding_extra_behaviour

def decorate_it_with_args_return(func):
    def adding_extra_behaviour(*args, **kwargs):
        print("**"*10)
        result = func(*args, **kwargs)
        print("**"*10)
        return result

    return adding_extra_behaviour