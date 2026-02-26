import functools
import inspect

i_deb =1

def debug(func):
    global i_deb
    print(f'I am debug ({i_deb})')
    i_deb += 1

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('I am wrapper')
        print(f'    Func name: {func.__name__}')
        print('    Args:')
        i=1
        for vals in inspect.signature(func).parameters.values():
            print(f'    {i}) {vals}')
        func(*args, **kwargs)

    return wrapper


@debug
def main_func(text: str):
    """
    My main function
    """
    print('I am main Func')
    print(text)

@debug
def add_2(a:int, b:int):
    print(f"The summ is: {a + b}")


main_func('Some words of main func ')
print()
print("_____________________________________________________________")
print()
add_2(b=1, a=6)
print()
print("_____________________________________________________________")
print()
add_2(14, 90)
