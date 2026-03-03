import functools

spc=" "
def call_limit(limit):
    print(f"Вызов call_limit. Ограничений запусков {limit}")
    def decorator(func):
        print(f"{spc*4}Декоратор. Программа: {func.__name__}. Лимитов осталось: {limit}")
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal limit
            if limit > 0:
                func(*args, **kwargs)
                limit -= 1
                print(f"{spc*8}Для программы {func.__name__} запусков осталось {limit}")
            else:
                print("!!!__________________________________________________________!!!")
                print(f"{spc*8}Превышено кол-во запусков для {func.__name__}")
                print("----------------------------------------------------------------")
                print()
        return wrapper
    return decorator

@call_limit(limit=3)
def send_email(address):
    print(f"{spc*12}Отправляю письмо на {address}")

@call_limit(limit=4)
def send_word(word):
    print(f"{spc*12}Отправляю слово {word}")

send_email("a@ex.com") # OK
send_word("Hello 1")
send_email("b@ex.com") # OK
send_word("Hello 2")
send_word("Hello 3")
send_email("c@ex.com") # OK
send_email("d@ex.com") # Вызовет ValueError
send_word("Hello 4")
send_word("Hello 5")
send_word("Hello 6")