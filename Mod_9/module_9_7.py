def is_prime(func):
    def add_phrase(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, result):
                if result % i == 0:
                    return f'Число {result} не является простым'
                return f'Число {result} простое'
        else:
            return f'Правила простых чисел не применимы с числам меньше 1'

    return add_phrase


@is_prime
def sum_three(one, two, three):
    return one + two + three


summa = sum_three(2, 3, 6)
print(summa, end='\n\n')

summa = sum_three(0, 0, 1)
print(summa, end='\n\n')

summa = sum_three(2, 4, 6)
print(summa, end='\n\n')